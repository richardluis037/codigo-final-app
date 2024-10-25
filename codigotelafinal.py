import flet as ft
import pyrebase #pip install pyrebase4


firebaseConfig = {
  'apiKey': "AIzaSyCpd2H2slbsA4co3jMEBNoU7k5gKOTALPI",
  'authDomain': "testelogin-3490d.firebaseapp.com",
  'projectId': "testelogin-3490d",
  'storageBucket': "testelogin-3490d.appspot.com",
  'databaseURL': "https:testelogin-3490d.firebaseio.com",
  'messagingSenderId': "503913986449",
  'appId': "1:503913986449:web:271c6672bad15387620230",
  'measurementId': "G-0NWTK4VN3L"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#Função que cria a página
def main(page: ft.page):
    page.title = "Meu App"
    page.window_width = 400
    page.window_height = 600
    page.bgcolor = 'white'
    page.theme_mode = 'white'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 20
    page.window.maximizable = False

    img = ft.Image(
        src=f"logocerta.svg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    def btn_voltar(e):
        page.add(usuario, senha, botao_logar, botao_novo)
        page.remove(botao_voltar)
        page.update()  

    def btn_login(e):
        try:
            auth.sign_in_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Login realizado com sucesso!"
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            usuario.value = None
            senha.value = None
            page.remove(usuario, senha, botao_logar, botao_novo)
            page.add(botao_voltar)
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Email ou senha inválidos"
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            page.update()
            
    def btn_novo(e):
        try:
            auth.create_user_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Usuário criado com sucesso!"
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            usuario.value = None
            senha.value = None
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Erro ao criar novo usuário!"
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            page.update()


    usuario = ft.TextField(
        hint_text = 'Email',
        label = 'Email',
        width = 200,
        border_color = 'black',
        color = 'black',
        label_style = ft.TextStyle(
            color = 'black' 
        )
    )
    senha = ft.TextField(
        hint_text='Senha',
        label='Senha',
        width=200,
        border_color='black',
        label_style=ft.TextStyle(
            color='black'
        ),
        password=True,
        can_reveal_password=True
    )
    botao_logar = ft.ElevatedButton(
        text='Login',
        color='white',
        bgcolor='black',
        width=200,
        height=50,
        on_click=btn_login
    )
    
    botao_novo = ft.ElevatedButton(
        text='Cadastrar novo usuário',
        color='white',
        bgcolor='black',
        width=200,
        height=50,
        on_click=btn_novo
    )
    botao_voltar = ft.ElevatedButton(
        text='Voltar',
        color='white',
        bgcolor='black',
        width=200,
        height=50,
        on_click= btn_voltar
    )
    count = 0
    def balao_msg(e):
        nonlocal count  # para modificar a variável de contagem encontrada no escopo externo
        page.open(ft.SnackBar(ft.Text("Uma empresa pensada para você")))
        count += 1

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.MESSAGE, on_click=balao_msg, bgcolor=ft.colors.BLACK)

    #Adiciona todos os elementos na página
    page.add(img, usuario, senha, botao_logar, botao_novo)


#Diz ao FLET que deve iniciar na função MAIN
ft.app(target=main)
    


