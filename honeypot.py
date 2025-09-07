import socket
import threading
import datetime

# Porta "isca" 
PORTA = 2222
IP = "0.0.0.0"  # Escuta em todas as interfaces
LOG_FILE = "honeypot_logs.txt"

def registrar_log(mensagem):
    """Salva logs em um arquivo com data e hora"""
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {mensagem}\n")

def lidar_com_cliente(conn, addr):
    """Simula um servidor vulnerável"""
    registrar_log(f"Conexão recebida de {addr}")

    # Mensagem de "boas-vindas" como se fosse um SSH falso
    conn.sendall(b"Bem-vindo ao servidor SSH Fake!\nLogin: ")

    try:
        login = conn.recv(1024).decode(errors="ignore").strip()
        registrar_log(f"Tentativa de login: {login}")

        conn.sendall(b"Senha: ")
        senha = conn.recv(1024).decode(errors="ignore").strip()
        registrar_log(f"Tentativa de senha: {senha}")

        # Resposta fake
        conn.sendall(b"Acesso negado.\n")
        registrar_log(f"Acesso negado para {addr}")

    except Exception as e:
        registrar_log(f"Erro ao lidar com cliente {addr}: {e}")

    conn.close()

def iniciar_honeypot():
    """Inicia o servidor Honeypot"""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP, PORTA))
    servidor.listen(5)
    print(f"Honeypot rodando na porta {PORTA}...")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_honeypot()
