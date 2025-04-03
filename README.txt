***** Eng *****

# PingToolServices

PingToolServices is a web-based tool developed with FastAPI that allows users to monitor the availability of websites in real-time. The system periodically checks if a website is online or offline and records downtime events, providing valuable insights for users.

## Features
- Real-time website monitoring
- Status updates on availability
- Downtime tracking (when the site goes down and how long it remains unavailable)
- Web interface for site management

## Installation

### Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- SQLite (built-in with Python)
- httpx (for website checking)

### Steps to Install and Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/PingToolServices.git
   cd PingToolServices
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   python -m uvicorn ping_tool_testes:app --host 0.0.0.0 --port 8000 --reload
   ```
4. Open the application in your browser:
   ```
   http://localhost:8000
   ```

## Running as a Windows Service
To ensure that the application runs in the background as a service:

1. Install NSSM (Non-Sucking Service Manager).
2. Run the following command:
   ```cmd
   nssm install PingToolServices
   ```
3. Set the Python script path as the executable.
4. Start the service:
   ```cmd
   net start PingToolServices
   ```

## Contributing
Feel free to fork this project, report issues, or suggest improvements. Contributions are welcome!

## License
This project is licensed under the MIT License.



***** PT-BR *****

# PingToolServices

## Sobre o Projeto
O **PingToolServices** é uma ferramenta de monitoramento de sites desenvolvida em **FastAPI**. Ele permite que o usuário verifique periodicamente o status de sites cadastrados, informando quando um site cai, por quanto tempo ficou offline e quando voltou ao ar. O sistema também conta com uma interface web para facilitar a visualização dos status em tempo real.

## Funcionalidades
- Monitoramento automático de sites.
- Exibição do status (online/offline) diretamente na interface web.
- Registro de quedas e tempo de inatividade.
- Pesquisa de sites para monitoramento.
- Atualização dinâmica dos status sem necessidade de recarregar a página.
- Execução como serviço de segundo plano no Windows.

## Tecnologias Utilizadas
- **Backend:** FastAPI, Uvicorn, SQLite, HTTPX
- **Frontend:** HTML, CSS, JavaScript (Fetch API)
- **Outros:** NSSM (para executar como serviço no Windows)

## Instalação e Execução
### 1. Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/PingToolServices.git
cd PingToolServices
```

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Iniciar o Servidor
```sh
python -m uvicorn ping_tool_testes:app --host 0.0.0.0 --port 8000 --reload
```

Acesse a interface web em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Executando como Serviço no Windows
Caso queira que o sistema rode automaticamente em segundo plano, siga os passos abaixo:

1. Baixe o **NSSM** [aqui](https://nssm.cc/download)
2. Extraia e abra o terminal na pasta extraída
3. Execute o comando abaixo para criar o serviço:
   ```sh
   nssm install PingToolServices
   ```
4. No campo **"Path"**, selecione o executável do Python.
5. No campo **"Startup directory"**, informe a pasta do projeto.
6. No campo **"Arguments"**, coloque:
   ```sh
   -m uvicorn ping_tool_testes:app --host 0.0.0.0 --port 8000
   ```
7. Clique em **Install service** e inicie o serviço via `services.msc`.

## Possíveis Melhorias Futuras
- Adicionar suporte a autenticação de usuários.
- Criar um dashboard mais detalhado com estatísticas.
- Implementar suporte para notificações via e-mail ou Telegram.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

## Contato
Caso tenha interesse em adaptações ou melhorias personalizadas para empresas, entre em contato via [LinkedIn](https://www.linkedin.com/in/seu-usuario/) ou pelo e-mail **seuemail@example.com**.

