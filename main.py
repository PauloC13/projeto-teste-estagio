from src.database import get_contacts
from src.zapi import send_message

def main():
    contacts = get_contacts(limit=3)

    if not contacts:
        print("Nenhum contato encontrado.")
        return
    for contact in contacts:
        name = contact["name"]
        phone = contact["phone"]

        message = f"Olá, {name} tudo bem com você?"

        try:
            send_message(phone, message)
            print(f"Mensagem enviada para {name} ({phone})")
        except Exception as e:
            print(f"Erro ao enviar para {name}: {e}")

if __name__ == "__main__":
    main()    