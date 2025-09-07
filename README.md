# 🕵️ Honeypot Simples em Python

Um **Honeypot** é uma técnica de segurança usada para **atrair atacantes** e **registrar tentativas de invasão** em um ambiente controlado.  
Este projeto implementa um honeypot básico em **Python**, simulando um servidor SSH falso que captura credenciais e interações dos invasores.


## 🚀 Funcionalidades
- Escuta conexões em uma porta definida (padrão: `2222`).
- Simula um **servidor SSH falso**.
- Registra:
  - IP do atacante
  - Tentativas de login
  - Tentativas de senha
- Gera logs em `honeypot_logs.txt`.


## 📂 Estrutura do Projeto

📦 honeypot
- 📜 honeypot.py
- 📜 honeypot_logs.txt # Gerado automaticamente
- 📜 README.md



## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/anyocher/honeypot.git
   cd honeypot

python3 honeypot.py

## 🔒 Aviso Importante
- Este projeto é apenas para fins educacionais ⚠️.
- Não utilize em ambientes de produção ou expostos à internet sem entender os riscos.
## 🛠 Melhorias Futuras
- Registro em banco de dados (SQLite/MongoDB).
- Dashboard web para visualizar ataques.
- Armadilhas realistas (diretórios e comandos falsos).
- Geolocalização dos IPs atacantes.
## 👨‍💻 Autor
Projeto desenvolvido por Any Ochner 📧 Contato: anyocher@outlook.com
