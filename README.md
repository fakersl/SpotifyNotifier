# SpotifyNotifier

[🇧🇷]**SpotifyNotifier** é uma ferramenta de notificação personalizável que permite monitorar a música atual tocando no seu Spotify e exibir notificações interativas diretamente na sua área de trabalho. A aplicação oferece uma experiência minimalista, mostrando a capa do álbum, o nome da música e o artista em uma janela flutuante discreta.

[🇺🇸]**SpotifyNotifier** is a customizable notification tool that allows you to monitor the current song playing on your Spotify and display interactive notifications directly on your desktop. The application offers a minimalist experience, showing the album cover, song name, and artist in a subtle floating window.

## Funcionalidades / Features

- [🇧🇷]**Notificação de música atual**: A cada nova música tocada no Spotify, a aplicação exibe uma notificação com informações sobre a faixa e o artista.  
  [🇺🇸]**Current Song Notification**: Every time a new song plays on Spotify, the application displays a notification with details about the track and artist.
  
- [🇧🇷]**Notificação personalizada**: Exibe a capa do álbum e informações da música na interface de forma clean e elegante.  
  [🇺🇸]**Customizable Notification**: Shows the album cover and song information in a clean and elegant interface.
  
- [🇧🇷]**Ajuste de posição**: Você pode mover a janela de notificação para diferentes partes da tela com um clique direito para personalização.  
  [🇺🇸]**Position Adjustment**: You can move the notification window to different parts of the screen with a right-click for customization.
  
- [🇧🇷]**Opção de iniciar com o sistema**: A aplicação pode ser configurada para iniciar automaticamente com o sistema no Windows.  
  [🇺🇸]**Auto-start with System**: The application can be configured to start automatically with the system on Windows.
  
- [🇧🇷]**Controle de execução**: Através da bandeja do sistema, o usuário pode fechar a aplicação ou mudar a posição da janela.  
  [🇺🇸]**Execution Control**: Through the system tray, users can close the application or change the position of the window.

## Tecnologias Utilizadas / Technologies Used

- [🇧🇷]**Python**: Linguagem de programação principal.  
  [🇺🇸]**Python**: Main programming language.
  
- [🇧🇷]**Spotipy**: Biblioteca para integração com a API do Spotify.  
  [🇺🇸]**Spotipy**: Library for integrating with the Spotify API.
  
- [🇧🇷]**Tkinter**: Framework para a criação de interfaces gráficas no Python.  
  [🇺🇸]**Tkinter**: Framework for creating graphical user interfaces in Python.
  
- [🇧🇷]**Pillow**: Biblioteca para manipulação de imagens, usada para exibir a capa do álbum.  
  [🇺🇸]**Pillow**: Library for image manipulation, used to display the album cover.
  
- [🇧🇷]**Pystray**: Biblioteca para criação de ícones de bandeja do sistema.  
  [🇺🇸]**Pystray**: Library for creating system tray icons.

## Instalação / Installation

### Executável / Executable

[🇧🇷]Se preferir, você pode baixar o executável diretamente na pasta `dist/` do repositório. O arquivo `app.exe` pode ser executado sem a necessidade de instalação das dependências do Python. Basta executar o arquivo para rodar a aplicação.  
[🇺🇸]If you prefer, you can download the executable directly from the `dist/` folder of the repository. The `app.exe` file can be run without the need to install Python dependencies. Just execute the file to run the application.

### Para rodar a versão em código (caso queira modificar ou rodar a versão sem o executável) / To run the code version (if you want to modify or run the version without the executable):

1. Clone o repositório / Clone the repository:

```bash
git clone https://github.com/fakersl/SpotifyNotifier.git
cd SpotifyNotifier
```

2. Instale as dependências necessárias com o `pip` / Install the necessary dependencies with `pip`:

```bash
pip install -r requirements.txt
```

3. Configure o Spotify / Configure Spotify:

[🇧🇷]Para usar a aplicação, você precisará configurar as credenciais do Spotify. Siga os passos abaixo:  
[🇺🇸]To use the application, you will need to configure Spotify credentials. Follow these steps:

- [🇧🇷]Acesse [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) e crie uma nova aplicação.  
  [🇺🇸]Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
  
- [🇧🇷]Copie o `Client ID` e `Client Secret` gerados e substitua no arquivo `app.py` nas variáveis `SPOTIFY_CLIENT_ID` e `SPOTIFY_CLIENT_SECRET`.  
  [🇺🇸]Copy the generated `Client ID` and `Client Secret`, and replace them in the `app.py` file in the `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` variables.
  
- [🇧🇷]Defina a URL de redirecionamento no Spotify como `http://localhost:8888/callback`.  
  [🇺🇸]Set the redirect URL in Spotify to `http://localhost:8888/callback`.

4. Execute a aplicação / Run the application:

```bash
python app.py
```

[🇧🇷]A aplicação iniciará e começará a monitorar sua conta do Spotify, exibindo notificações quando uma nova música começar a tocar.  
[🇺🇸]The application will start and begin monitoring your Spotify account, displaying notifications when a new song starts playing.

## Funcionalidade de Iniciar com o Sistema / Auto-start with System

Caso deseje que o programa seja iniciado automaticamente com o Windows:  
[🇺🇸]If you want the program to start automatically with Windows:

1. [🇧🇷]No código, a função `add_to_startup()` já está configurada para adicionar a aplicação ao processo de inicialização do sistema.  
   [🇺🇸]In the code, the `add_to_startup()` function is already set to add the application to the system startup process.
   
2. [🇧🇷]Descomente a chamada `add_to_startup()` na linha 146 do `app.py`.  
   [🇺🇸]Uncomment the call to `add_to_startup()` at line 146 of `app.py`.

## Contribuição / Contribution

[🇧🇷]Sinta-se à vontade para fazer um fork deste repositório, abrir issues ou enviar pull requests para melhorar a aplicação. Sua contribuição é sempre bem-vinda!  
[🇺🇸]Feel free to fork this repository, open issues, or submit pull requests to improve the application. Your contribution is always welcome!

1. Fork o repositório. / Fork the repository.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`). / Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Faça suas alterações e faça commit delas (`git commit -am 'Adiciona nova feature'`). / Make your changes and commit them (`git commit -am 'Adds new feature'`).
4. Envie para a branch principal (`git push origin feature/nova-feature`). / Push to the main branch (`git push origin feature/new-feature`).
5. Abra um Pull Request. / Open a Pull Request.

## Licença / License

[🇧🇷]Este projeto está licenciado sob a Licença Apache - veja o arquivo [LICENSE](LICENSE) para mais detalhes.  
[🇺🇸]This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for more details.

---

💻 [🇧🇷]Desenvolvido por **[Gustavo Santos](https://github.com/fakersl)**.  
💻 [🇺🇸]Developed by **[Gustavo Santos](https://github.com/fakersl)**.
