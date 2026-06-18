# WhatsApp Sender

Script em Python que lê contatos cadastrados no **Supabase** e envia uma mensagem personalizada via **Z-API** para cada um deles.


## 📋 Sobre o projeto

O script:
1. Conecta no banco de dados do Supabase
2. Busca até 3 contatos cadastrados na tabela `contacts`
3. Para cada contato, monta a mensagem `"Olá, <nome_contato> tudo bem com você?"`
4. Envia a mensagem via WhatsApp usando a API do Z-API

## 🛠️ Tecnologias

- [Python 3.12](https://www.python.org/)
- [Supabase](https://supabase.com/) — banco de dados PostgreSQL na nuvem
- [Z-API](https://www.z-api.io/) — API para envio de mensagens via WhatsApp
- [python-dotenv](https://pypi.org/project/python-dotenv/) — leitura de variáveis de ambiente
- [requests](https://pypi.org/project/requests/) — chamadas HTTP

## 🗄️ Setup da tabela no Supabase

Crie uma tabela chamada `contacts` com as colunas:

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | int8 | Chave primária (gerada automaticamente) |
| `name` | text | Nome do contato |
| `phone` | text | Número do WhatsApp, com DDI e DDD (ex: `5585999999999`) |
| `created_at` | timestamp | Data de criação (gerada automaticamente) |

Insira de 1 a 3 contatos de teste na tabela.

## 🔑 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-anon-key
ZAPI_INSTANCE=id-da-sua-instancia
ZAPI_TOKEN=token-da-instancia
ZAPI_CLIENT_TOKEN=client-token-de-seguranca
```

| Variável | Onde encontrar |
|---|---|
| `SUPABASE_URL` | Painel do Supabase → Project Settings → API → Project URL |
| `SUPABASE_KEY` | Painel do Supabase → Project Settings → API → anon public key |
| `ZAPI_INSTANCE` | Painel do Z-API → ID da instância |
| `ZAPI_TOKEN` | Painel do Z-API → Token da instância |
| `ZAPI_CLIENT_TOKEN` | Painel do Z-API → Segurança → Token de segurança da conta (precisa ser ativado) |

## ▶️ Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/guilhermeoliveira-software/whatsapp-sender.git
cd whatsapp-sender
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o `.env` (veja a seção acima)

5. Execute o script:
```bash
python main.py
```

## 📦 Estrutura do projeto

```
whatsapp-sender/
├── main.py            # Código principal
├── requirements.txt   # Dependências do projeto
├── .env.example        # Modelo de variáveis de ambiente
├── .gitignore
└── README.md
```

## ✅ Saída esperada

```
🔍 Buscando contatos no Supabase...
✅ 1 contato(s) encontrado(s).

📤 Enviando mensagem para Guilherme (85997258174)...
✅ Mensagem enviada com sucesso para Guilherme!
```
