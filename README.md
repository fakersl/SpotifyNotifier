# SpotifyNotifier

**SpotifyNotifier** é uma ferramenta de notificação personalizável que permite monitorar a música atual tocando no seu Spotify e exibir notificações interativas diretamente na sua área de trabalho. A aplicação oferece uma experiência minimalista, mostrando a capa do álbum, o nome da música e o artista em uma janela flutuante discreta.

## Funcionalidades

- **Notificação de música atual**: A cada nova música tocada no Spotify, a aplicação exibe uma notificação com informações sobre a faixa e o artista.
- **Notificação personalizada**: Exibe a capa do álbum e informações da música na interface de forma clean e elegante.
- **Ajuste de posição**: Você pode mover a janela de notificação para diferentes partes da tela com um clique direito para personalização.
- **Opção de iniciar com o sistema**: A aplicação pode ser configurada para iniciar automaticamente com o sistema no Windows.
- **Controle de execução**: Através da bandeja do sistema, o usuário pode fechar a aplicação ou mudar a posição da janela.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Spotipy**: Biblioteca para integração com a API do Spotify.
- **Tkinter**: Framework para a criação de interfaces gráficas no Python.
- **Pillow**: Biblioteca para manipulação de imagens, usada para exibir a capa do álbum.
- **Pystray**: Biblioteca para criação de ícones de bandeja do sistema.

## Instalação

### Executável

Se preferir, você pode baixar o executável diretamente na pasta `dist/` do repositório. O arquivo `app.exe` pode ser executado sem a necessidade de instalação das dependências do Python. Basta executar o arquivo para rodar a aplicação.

### Para rodar a versão em código (caso queira modificar ou rodar a versão sem o executável):

1. Clone o repositório:

```bash
git clone https://github.com/fakersl/SpotifyNotifier.git
cd SpotifyNotifier
```

2. Instale as dependências necessárias com o `pip`:

```bash
pip install -r requirements.txt
```

3. Configure o Spotify:

Para usar a aplicação, você precisará configurar as credenciais do Spotify. Siga os passos abaixo:

- Acesse [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) e crie uma nova aplicação.
- Copie o `Client ID` e `Client Secret` gerados e substitua no arquivo `app.py` nas variáveis `SPOTIFY_CLIENT_ID` e `SPOTIFY_CLIENT_SECRET`.
- Defina a URL de redirecionamento no Spotify como `http://localhost:8888/callback`.

4. Execute a aplicação:

```bash
python app.py
```

A aplicação iniciará e começará a monitorar sua conta do Spotify, exibindo notificações quando uma nova música começar a tocar.

## Funcionalidade de Iniciar com o Sistema

Caso deseje que o programa seja iniciado automaticamente com o Windows:

1. No código, a função `add_to_startup()` já está configurada para adicionar a aplicação ao processo de inicialização do sistema.
2. Descomente a chamada `add_to_startup()` na linha 146 do `app.py`.

## Screenshots

Aqui estão algumas capturas de tela de como a aplicação se parece quando uma música está sendo tocada:

![SpotifyNotifier](screenshots/spotify-notifier.png)

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório, abrir issues ou enviar pull requests para melhorar a aplicação. Sua contribuição é sempre bem-vinda!

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça suas alterações e faça commit delas (`git commit -am 'Adiciona nova feature'`).
4. Envie para a branch principal (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença Apache - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com 💻 por **[Gustavo Santos](https://github.com/fakersl)**.
```
