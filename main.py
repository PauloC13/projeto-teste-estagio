from src.database import get_contacts

def main():
    contacts = get_contacts(limit=3)

    if not contacts:
        print("Nenhum contato encontrado.")
        return
    else:
        print(contacts)

if __name__ == "__main__":
    main()    