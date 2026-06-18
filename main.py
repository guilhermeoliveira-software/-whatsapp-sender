import os
import requests
from supabase import create_client
from dotenv import load_dotenv


load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    """Busca até 3 contatos cadastrados no Supabase."""
    response = supabase.table("contacts").select("*").limit(3).execute()
    return response.data


def enviar_mensagem(phone, nome):
    """Envia mensagem personalizada via Z-API."""
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
    headers = {
    "Client-Token": ZAPI_CLIENT_TOKEN
}
    payload = {
        "phone": phone,
        "message": f"Olá, {nome} tudo bem com você?"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response


def main():
    print("🔍 Buscando contatos no Supabase...")
    contatos = buscar_contatos()

    if not contatos:
        print("❌ Nenhum contato encontrado no banco de dados.")
        return

    print(f"✅ {len(contatos)} contato(s) encontrado(s).\n")

    for contato in contatos:
        nome = contato.get("name")
        phone = contato.get("phone")

        print(f"Enviando mensagem para {nome} ({phone})...")

        try:
            response = enviar_mensagem(phone, nome)
            if response.status_code == 200:
                print(f"✅ Mensagem enviada com sucesso para {nome}!\n")
            else:
                print(f"⚠️ Erro ao enviar para {nome}: {response.status_code} - {response.text}\n")
        except Exception as e:
            print(f"❌ Erro inesperado ao enviar para {nome}: {e}\n")

if _name_ == "_main_":
    main()
