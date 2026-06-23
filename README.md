# Supabase + Z-API Sender

Projeto que lê contatos do Supabase e envia mensagens personalizadas usando a Z-API.

## Requisitos

- Python 3.10+
- Conta gratuita Supabase
- Conta gratuita Z-API

## Estrutura da tabela

```sql
create table contacts (
    id bigint generated always as identity primary key,
    name text not null,
    phone text not null
);
```

## Variáveis de ambiente

Copie:

```bash
cp .env.example .env
```

Preencha:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

O sistema busca até 3 contatos do Supabase e envia:

Olá, <nome_contato> tudo bem com você?