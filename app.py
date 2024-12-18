import time
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageTk
import tkinter as tk
import os
import sys
import winreg as reg
from pystray import Icon, MenuItem, Menu
from threading import Thread

# Configuração do Spotify
SPOTIFY_CLIENT_ID = "835c1bdf95e0421a8a3338ea0c824e93"
SPOTIFY_CLIENT_SECRET = "1e9449d45006435fb0a3e6cc379098c0"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="user-read-playback-state"))

# Variável global para manter a janela ativa
current_window = None
current_position = "top-left"  # Posição inicial da janela

# Função para adicionar o programa ao iniciar o PC (apenas no Windows)
def add_to_startup():
    try:
        key = reg.HKEY_CURRENT_USER
        path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = reg.OpenKey(key, path, 0, reg.KEY_WRITE)
        reg.SetValueEx(reg_key, "SpotifyNoticador", 0, reg.REG_SZ, sys.executable + " " + sys.argv[0])
        reg.CloseKey(reg_key)
    except Exception as e:
        print(f"Erro ao adicionar ao iniciar o PC: {e}")

# Função para baixar e salvar a imagem da capa
def download_album_cover(img_url):
    img_path = "album_cover.png"
    response = requests.get(img_url, stream=True)
    if response.status_code == 200:
        with open(img_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    return img_path

# Função para exibir a notificação
def show_custom_notification(song, artist, album_img_url):
    global current_window, current_position

    if current_window is not None:
        try:
            if current_window.winfo_exists():
                current_window.destroy()
        except tk.TclError:
            pass

    img_path = download_album_cover(album_img_url)

    window = tk.Tk()
    window.title("Tocando agora")
    window.geometry("350x120")  # Tamanho fixo
    window.overrideredirect(True)
    window.attributes('-topmost', True)
    window.attributes('-alpha', 0.0)

    # Configurar posição
    if current_position == "top-left":
        window.geometry("+10+10")
    elif current_position == "top-right":
        window.geometry("+1200+10")  # Ajuste a posição conforme necessário
    elif current_position == "bottom-left":
        window.geometry("+10+800")
    elif current_position == "bottom-right":
        window.geometry("+1200+800")  # Ajuste a posição conforme necessário

    window.configure(bg="white")

    img = Image.open(img_path).resize((100, 100))
    img_tk = ImageTk.PhotoImage(img)

    cover_label = tk.Label(window, image=img_tk, bg="white")
    cover_label.image = img_tk
    cover_label.pack(side="left", padx=10, pady=10)

    info_frame = tk.Frame(window, bg="white")
    info_frame.pack(side="right", fill="both", expand=True)

    # Texto "Tocando agora:"
    playing_label = tk.Label(info_frame, text="Tocando agora:", font=("Helvetica", 10, "italic"), bg="white", fg="gray")
    playing_label.pack(anchor="w", pady=(5, 0))

    song_label = tk.Label(info_frame, text=song, font=("Helvetica", 12, "bold"), bg="white")
    song_label.pack(anchor="w", pady=(5, 0))

    artist_label = tk.Label(info_frame, text=artist, font=("Helvetica", 10), bg="white", fg="gray")
    artist_label.pack(anchor="w")

    # Função de fade-in
    def fade_in(alpha=0.0):
        if alpha < 1.0:
            alpha += 0.05
            window.attributes('-alpha', alpha)
            window.after(30, lambda: fade_in(alpha))
        else:
            window.after(4000, fade_out)

    # Função de fade-out
    def fade_out(alpha=1.0):
        if alpha > 0.0:
            alpha -= 0.05
            window.attributes('-alpha', alpha)
            window.after(30, lambda: fade_out(alpha))
        else:
            window.destroy()
            os.remove(img_path)

    def open_menu(event):
        menu = tk.Menu(window, tearoff=0)
        menu.add_command(label="Mover para Canto Superior Esquerdo", command=lambda: set_position("top-left"))
        menu.add_command(label="Mover para Canto Superior Direito", command=lambda: set_position("top-right"))
        menu.add_command(label="Mover para Canto Inferior Esquerdo", command=lambda: set_position("bottom-left"))
        menu.add_command(label="Mover para Canto Inferior Direito", command=lambda: set_position("bottom-right"))
        menu.add_command(label="Fechar", command=window.destroy)
        menu.post(event.x_root, event.y_root)

    # Função para alterar a posição da janela
    def set_position(position):
        global current_position
        current_position = position
        window.destroy()
        show_custom_notification(song, artist, album_img_url)

    window.bind("<Button-3>", open_menu)  # Clique com o botão direito para abrir o menu

    fade_in()

    current_window = window

    window.mainloop()


# Monitorar a música atual
def monitor_spotify(interval=1):
    last_song = ""
    while True:
        try:
            current_track = sp.current_playback()
            if current_track and current_track['item']:
                song = current_track['item']['name']
                artist = ", ".join(a['name'] for a in current_track['item']['artists'])
                album_img_url = current_track['item']['album']['images'][0]['url']

                if song != last_song:
                    show_custom_notification(song, artist, album_img_url)
                    last_song = song
        except Exception as e:
            print(f"Erro: {e}")
        time.sleep(interval)

# Função para esconder a janela e deixá-la na bandeja
def on_quit(icon, item):
    icon.stop()

# Função para criar o ícone na bandeja
def create_icon():
    icon_image = Image.open("icon.jpg")  # Substitua por sua imagem de ícone
    icon = Icon("SpotifyNotify", icon_image, menu=Menu(MenuItem("Sair", on_quit)))
    icon.run()

# Executar ao iniciar o PC (opcional)
if __name__ == "__main__":
    add_to_startup()  # Descomente para adicionar ao iniciar o PC

    # Iniciar a monitorização em uma thread separada
    spotify_thread = Thread(target=monitor_spotify)
    spotify_thread.daemon = True
    spotify_thread.start()

    # Criar o ícone na bandeja
    create_icon()