import ping3
import time
import smtplib
from email.mime.text import MIMEText
import socket

# 🔹 Lista de sites/IPs para monitorar (adicione os seus aqui)
HOSTS = ["google.com", "8.8.8.8", "github.com", "sitequenaashuhejlasl.com"]

# 🔹 Configuração do e-mail (altere para seu e-mail e senha)
EMAIL_SENDER = "jhonsantx@gmail.com"
EMAIL_PASSWORD = "qhdt kfle ljyk jzau"  # ⚠️ Melhor usar senha de app para segurança
EMAIL_RECEIVER = "jhonsantx@gmail.com"

def send_email(host):
    """Envia um e-mail de alerta quando um site cai."""
    subject = f"⚠️ Alerta: {host} está offline!"
    body = f"O site/IP {host} não respondeu ao ping e pode estar fora do ar."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"📧 Alerta enviado para {EMAIL_RECEIVER} sobre {host}!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

def ping_host(host):
    """Verifica se o host responde ao ping e se o DNS é válido."""
    try:
        # 🔹 Primeiro, tenta resolver o DNS (se falhar, o site é inválido)
        socket.gethostbyname(host)
        
        # 🔹 Agora faz o ping
        response_time = ping3.ping(host, timeout=2)
        if response_time is None:
            return False  # Se não houver resposta, o site está offline
        return True
    except (socket.gaierror, Exception):  # Erro se o site for inválido
        return False

def main():
    offline_hosts = set()  # Armazena os sites que já caíram (evita e-mails repetidos)

    while True:  # 🔄 Loop infinito
        with open("ping_log.txt", "a") as log:
            log.write(f"\n--- Ping Test - {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            
            for host in HOSTS:
                online = ping_host(host)
                
                if online:
                    print(f"✅ {host} está online.")
                    log.write(f"{host} está online.\n")
                    if host in offline_hosts:
                        offline_hosts.remove(host)  # Remove da lista de offline
                else:
                    print(f"❌ {host} está offline!")
                    log.write(f"{host} está offline!\n")

                    if host not in offline_hosts:  # Só envia e-mail se for a primeira vez que caiu
                        send_email(host)
                        offline_hosts.add(host)  # Marca como offline para evitar alertas repetidos

        time.sleep(60)  # 🔄 Espera 60 segundos antes de repetir o processo

if __name__ == "__main__":
    main()
