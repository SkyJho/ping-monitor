import os

# Encerra todos os processos do FastAPI
os.system("taskkill /IM python.exe /F")
print("✅ FastAPI foi encerrado!")
