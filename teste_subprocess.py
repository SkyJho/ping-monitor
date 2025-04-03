import subprocess
import sys

python_exe = sys.executable

# Teste executando um comando básico
subprocess.Popen([python_exe, "-c", "print('Subprocess está rodando!')"])
