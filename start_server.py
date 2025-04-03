import subprocess
import os

# Caminho do Python e do script FastAPI
python_exe = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "WindowsApps", "python.exe")
script_path = os.path.abspath("C:\\MeusProjetos\\Python Contra_Com\\ping_tool_testes.py")

# Iniciar o servidor FastAPI
subprocess.Popen([python_exe, "-m", "uvicorn", "ping_tool_testes:app", "--host", "0.0.0.0", "--port", "80"], 
                 creationflags=subprocess.CREATE_NO_WINDOW)
