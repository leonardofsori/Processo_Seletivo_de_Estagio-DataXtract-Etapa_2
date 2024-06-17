import random
import time
import socket

tabela_nova = str(input("Deseja criar um novo arquivo para os dados? [S/N]: "))
while tabela_nova != "S" and tabela_nova != "s" and tabela_nova != "N" and tabela_nova != "n":
    tabela_nova = str(input("Insira uma resposta valida! [S/N]: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Função para criar novo objeto de socket onde será utilizado a arquitetura TCP/IP (IPv4)
host = socket.gethostname() # O Host/IPv4 utilizado é da maquina que está rodando o algoritmo
port = 8080 

client_socket.connect((host, port)) # Conecta ao servidor
client_socket.send(tabela_nova.encode())
resposta = client_socket.recv(1024)
print("Mensagem do servidor:", resposta.decode())

def dados_simulados():
    dados = {
        "velocidade": round(random.uniform(0, 200), 2),                             # Definindo uma velocidade aleatória entre 0 a 200 Km/h
        "temperatura_motor": round(random.uniform(60, 120), 2),                     # Definindo uma temperatura do motor aleatória entre 60 a 120 ºC  
        "pressao_pneu_dianteiro_esquerdo": round(random.uniform(25, 40), 2),        # Definindo uma pressão do pneu dianteiro esquerdo aleatória entre 25 a 40 PSI
        "pressao_pneu_dianteiro_direito": round(random.uniform(25, 40), 2),         # Definindo uma pressão do pneu dianteiro direito aleatória entre 25 a 40 PSI
        "pressao_pneu_traseiro_esquerdo": round(random.uniform(25, 40), 2),         # Definindo uma pressão do pneu traseiro esquerdo aleatória entre 25 a 40 PSI
        "pressao_pneu_traseiro_direito": round(random.uniform(25, 40), 2),          # Definindo uma pressão do pneu traseiro direito aleatória entre 25 a 40 PSI
        "rpm": round(random.uniform(0, 7000), 2),                                   # Definindo uma rotação por minuto aleatória entre 0 a 7000 RPM
        "nivel_combustivel": round(random.uniform(0, 100), 2),                      # Definindo uma quantidade de combustivel aleatória entre 0% a 100%
        "odometro": round(random.uniform(0, 200000), 2),                            # Definindo uma distância percorrida aleatória entre 0 a 200000 Km
        "status_farol": random.choice([True, False])                                # Definindo se o farol está ligado ou desligado
    }
    return dados

# Loop para simular a coleta contínua de dados
while True:
    dados_coletados = dados_simulados()                 # Armazena os dados simulados/medidos em uma variavel
    print("\nDados coletados:", dados_coletados)     # Imprime o resultado dos dados simulados/medidos para o usuário
    msg = str(dados_coletados)                          # Transoforma os dados simulados/medidos em uma string para enviar para o servidor
    client_socket.send(msg.encode())                    # Envia os dados do coletor até o servidor (utilizando o encode para transformar a string em bytes)
    time.sleep(0.5)                                       # Intervalo de tempo entre as coletas (simulado em segundos)
