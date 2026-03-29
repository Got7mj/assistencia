erDiagram
    PESSOA {
        int id PK
        string nome
        date data_nasc
        int endereco_id FK
    }

    CONTATO {
        int id PK
        string telefone
        string email
        string whatsapp
        int pessoa_id FK
    }

    ENDERECO {
        int id PK
        string rua
        string numero
        string bairro
        string cidade
        string estado
    }

    CLIENTE {
        int id_cliente PK, FK
    }

    FUNCIONARIO {
        int id_funcionario PK, FK
        float salario
        string carteira_de_trabalho
        string horario_expediente
        int cargo_id FK
    }

    CARGO {
        int id PK
        string nome
        float salario_base
    }

    ORDEM_SERVICO {
        int id PK
        int cliente_id FK
        int funcionario_id FK
        date data_emissao
        date data_inicio
        float valor_total
        string situacao
        string descricao
    }

    ITEM_OS {
        int id PK
        string descricao
        int quantidade
        int ordem_servico_id FK
        int equipamento_id FK
    }

    EQUIPAMENTO {
        int id PK
        string tipo
        string marca
        string modelo
        int quantidade
    }

    VISITA_TECNICA {
        int id PK
        int ordem_id FK
        int funcionario_id FK
        string horario
    }

    CONTA_RECEBER {
        int id PK
        int ordem_id FK
        float valor
        date data_pagamento
        float acrescimo
    }

    PAGAMENTO {
        int id PK
        int conta_id FK
        date data_pagamento
        float valor
    }

    %% RELACIONAMENTOS
    PESSOA ||--o{ CONTATO : possui    
    PESSOA ||--|| CLIENTE : especializa
    PESSOA ||--|| FUNCIONARIO : especializa
    ENDERECO ||--o{ PESSOA : possui

    CARGO ||--|{ FUNCIONARIO : possui
    CLIENTE ||--|{ ORDEM_SERVICO : solicita
    FUNCIONARIO ||--o{ ORDEM_SERVICO : executa
    ORDEM_SERVICO ||--|{ ITEM_OS : contem
    EQUIPAMENTO ||--|{ ITEM_OS : compoe
    ORDEM_SERVICO ||--|{ VISITA_TECNICA : gera
    FUNCIONARIO ||--|{ VISITA_TECNICA : realiza
    ORDEM_SERVICO ||--|| CONTA_RECEBER : gera
    CONTA_RECEBER ||--o{ PAGAMENTO : recebe
