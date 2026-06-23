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
SUPABASE_URL=https://tikwpwqjfxltetxrzlou.supabase.co
SUPABASE_KEY=sb_publishable_d1WI980FEn35IlHyDvkXBg_uoY_phzH

ZAPI_INSTANCE_ID=3F509C8E6F4B32E77C23D2DE7131D002
ZAPI_TOKEN=A00DD833D1D88E77B1942308
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