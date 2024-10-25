## Sistema de Upload Assíncrono para SharePoint

Este sistema permite o upload de arquivos grandes para o SharePoint de forma assíncrona, utilizando Flask como backend e a biblioteca Office 365 para Python.

**Funcionalidades:**

- Upload assíncrono de arquivos grandes para o SharePoint.
- Divisão do arquivo em partes menores (chunks) para otimizar o processo de upload.
- Interface simples via API REST para enviar arquivos.
- Armazenamento temporário do arquivo localmente antes do upload.
- Remoção automática do arquivo temporário após o upload.
- Feedback sobre o progresso do upload.

**Arquitetura:**

O sistema é composto por três componentes principais:

1.  **SharePointClient:** Responsável pela comunicação com o SharePoint, incluindo autenticação e upload de arquivos.
2.  **SharePointConfig:** Armazena as configurações de conexão com o SharePoint.
3.  **API Flask:** Fornece um endpoint `/upload` para receber arquivos via requisições POST.

**Fluxo de Upload:**

1.  O usuário envia um arquivo para o endpoint `/upload`.
2.  A API Flask salva o arquivo temporariamente no servidor.
3.  Uma tarefa assíncrona é criada para realizar o upload do arquivo para o SharePoint.
4.  O `SharePointClient` se autentica no SharePoint e inicia o upload do arquivo em partes (chunks).
5.  A cada chunk enviado, o progresso do upload é exibido no console.
6.  Após o upload completo, o arquivo temporário é removido do servidor.
7.  A API Flask retorna uma mensagem de sucesso para o usuário.

**Configuração:**

1.  **SharePointConfig:**

    - `site_url`: URL do site do SharePoint.
    - `username`: Nome de usuário para autenticação no SharePoint.
    - `password`: Senha para autenticação no SharePoint.
    - `folder_url`: URL da pasta no SharePoint onde os arquivos serão salvos.

2.  **API Flask:**

    - A API Flask é executada na porta 5000 por padrão.
    - O endpoint `/upload` aceita requisições POST com um arquivo no corpo da requisição.

**Dependências:**

- `office365`: Biblioteca para interagir com o SharePoint.
- `flask`: Framework web para Python.

**Instalação:**

1.  Instale as dependências:

```bash
pip install office365 flask
```

Use o código [com cuidado](/faq#coding).

2.  Configure as credenciais do SharePoint no arquivo `config.sharepoint_config.py`.
3.  Execute a aplicação Flask:

```bash
python app.py
```

Use o código [com cuidado](/faq#coding).

**Observações:**

- O tamanho do chunk (100 MB) pode ser ajustado conforme necessário.
- O sistema utiliza autenticação básica para se conectar ao SharePoint.
- É importante garantir que as credenciais do SharePoint estejam seguras e não sejam expostas no código.
# ShareUplift
