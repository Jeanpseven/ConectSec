import paramiko
import os
from ftplib import FTP

def conectar_ssh():
    host = input("Digite o endereço do servidor SSH: ")
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha (deixe em branco para autenticação sem senha): ")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if password:
            client.connect(hostname=host, username=username, password=password)
        else:
            client.connect(hostname=host, username=username)
        print("Conexão SSH estabelecida com sucesso!")
        # Faça outras operações ou comandos SSH aqui

        client.close()

    except paramiko.AuthenticationException:
        print("Falha na autenticação. Verifique as credenciais.")
    except paramiko.SSHException as e:
        print(f"Erro ao estabelecer conexão SSH: {str(e)}")
    except paramiko.SSHException:
        print("Erro desconhecido ao estabelecer conexão SSH.")

def abrir_servidor_ssh():
    porta = input("Digite a porta para abrir o servidor SSH: ")
    senha = input("Digite uma senha para autenticação (deixe em branco para autenticação sem senha): ")

    try:
        server = paramiko.Transport(('', int(porta)))
        if senha:
            server.set_password(senha)
        server.start_server()
        print(f"Servidor SSH aberto na porta {porta}. Aguardando conexões...")

        # Faça outras operações ou tratamentos de conexões aqui

        server.close()

    except paramiko.SSHException as e:
        print(f"Erro ao abrir servidor SSH: {str(e)}")
    except Exception as e:
        print(f"Erro desconhecido ao abrir servidor SSH: {str(e)}")

def conectar_netcat():
    host = input("Digite o endereço do servidor Netcat: ")
    porta = input("Digite a porta do servidor Netcat: ")

    try:
        os.system(f"nc {host} {porta}")
    except Exception as e:
        print(f"Erro ao conectar com o servidor Netcat: {str(e)}")

def abrir_vnc():
    opcao = input("Digite 1 para conectar a um servidor VNC existente ou 2 para abrir um novo servidor VNC: ")

    if opcao == "1":
        host = input("Digite o endereço do servidor VNC: ")
        porta = input("Digite a porta do servidor VNC: ")

        try:
            os.system(f"vncviewer {host}:{porta}")
            print(f"Conectado ao servidor VNC {host}:{porta}")
        except Exception as e:
            print(f"Erro ao conectar ao servidor VNC: {str(e)}")

    elif opcao == "2":
        porta = input("Digite a porta para abrir o servidor VNC: ")

        try:
            os.system(f"vncserver :{porta}")
            print(f"Servidor VNC aberto na porta {porta}. Aguardando conexões...")
        except Exception as e:
            print(f"Erro ao abrir servidor VNC: {str(e)}")

    else:
        print("Opção inválida. Tente novamente.")

def conectar_ftp():
    opcao = input("Digite 1 para conectar a um servidor FTP existente ou 2 para abrir um novo servidor FTP: ")

    if opcao == "1":
        host = input("Digite o endereço do servidor FTP: ")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")

        try:
            ftp = FTP(host)
            ftp.login(username, password)
            print("Conexão FTP estabelecida com sucesso!")
            # Faça outras operações ou comandos FTP aqui

            ftp.quit()

        except Exception as e:
            print(f"Erro ao estabelecer conexão FTP: {str(e)}")

    elif opcao == "2":
        porta = input("Digite a porta para abrir o servidor FTP: ")
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")

        try:
            server = FTP()
            server.set_debuglevel(2)
            server.bind(('', int(porta)))
            server.login(username, password)
            print(f"Servidor FTP aberto na porta {porta}. Aguardando conexões...")
            # Faça outras operações ou tratamentos de conexões aqui

            server.close()

        except Exception as e:
            print(f"Erro ao abrir servidor FTP: {str(e)}")

    else:
        print("Opção inválida. Tente novamente.")

def exibir_menu():
    print("========== MENU DE CONEXÃO ==========")
    print("1. Conectar a um servidor SSH")
    print("2. Abrir um servidor SSH")
    print("3. Conectar usando Netcat")
    print("4. Abrir ou conectar a um servidor VNC")
    print("5. Abrir ou conectar a um servidor FTP")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opção (1-6): ")

        if opcao == "1":
            conectar_ssh()
        elif opcao == "2":
            abrir_servidor_ssh()
        elif opcao == "3":
            conectar_netcat()
        elif opcao == "4":
            abrir_vnc()
        elif opcao == "5":
            conectar_ftp()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
