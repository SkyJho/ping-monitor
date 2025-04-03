import subprocess
import os
import sys
import time

# Caminho correto do Python
python_exe = sys.executable  # Obtém automaticamente o caminho correto do Python

# Diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Criar um arquivo de log para capturar erros
log_file = os.path.join(script_dir, "pingtool_log.txt")

# Tentar iniciar o FastAPI
with open(log_file, "w") as log:
    process = subprocess.Popen(
        [python_exe, "-m", "uvicorn", "ping_tool_testes:app", "--host", "0.0.0.0", "--port", "8080"],
        cwd=script_dir,
        stdout=log,   # Captura logs no arquivo
        stderr=log,   # Captura erros no arquivo
        creationflags=subprocess.CREATE_NO_WINDOW  # Mantém invisível
    )

# Esperar alguns segundos para garantir que o servidor iniciou
time.sleep(3)

# Teste se o processo ainda está rodando
if process.poll() is None:
    print("✅ FastAPI iniciado com sucesso!")
else:
    print("❌ Erro ao iniciar FastAPI. Veja o arquivo pingtool_log.txt")
