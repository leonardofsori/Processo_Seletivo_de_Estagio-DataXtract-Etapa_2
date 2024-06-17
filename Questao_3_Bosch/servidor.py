import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Função para criar novo objeto de socket onde será utilizado a arquitetura TCP/IP (IPv4)
host = socket.gethostname() # O Host/IPv4 utilizado é da maquina que está rodando o algoritmo
port = 8080

server_socket.bind((host, port)) # Cria um servidor
server_socket.listen(500)        # Servidor aguarda por conexão
print("Aguardando conexões...") 

client_socket, addr = server_socket.accept() # Servidor recebe a solicitação e aceita a sincronização
print("Conexão recebida de ", addr)
    
tabela = client_socket.recv(1024)
tabela = tabela.decode()

if tabela == "S" or tabela == "s":
    with open("dados_obtidos.csv", mode="w") as create:
        aux = "velocidade" + ",temperatura motor" + ",pressao pneu dianteiro esquerdo" + ",pressao pneu dianteiro direito" + ",pressao pneu traseiro esquerdo" + ",pressao pneu traseiro direito"+ ",rpm" + ",nivel combustivel"+ ",odometro" + ",status farol\n"
        create.write(aux)
        mensagem1 = "Arquivo novo criado!"
        client_socket.send(mensagem1.encode())
        
elif tabela == "N" or tabela == "n":
    try:     
        with open("dados_obtidos.csv", mode="r") as file:
            mensagem2 = "Arquivo antigo mantido!"
            client_socket.send(mensagem2.encode())

    except IOError:
        with open("dados_obtidos.csv", mode="w") as create:
            aux = "velocidade" + ",temperatura motor" + ",pressao pneu dianteiro esquerdo" + ",pressao pneu dianteiro direito" + ",pressao pneu traseiro esquerdo" + ",pressao pneu traseiro direito"+ ",rpm" + ",nivel combustivel"+ ",odometro" + ",status farol\n"
            create.write(aux)
            mensagem3 = "Não havia arquivo antigo, arquivo novo criado!"
            client_socket.send(mensagem3.encode())
            
while True:
    dados = client_socket.recv(1024) # Servidor recebe os dados simulados/medidos do coletor
    
    if dados != None:
        print("Mensagem armazena no arquivo CSV")
        dados_string = dados.decode()                        # Armazenar os dados decodificados em uma variavel
        dados_string = dados_string[1:len(dados_string)-1]   # Tratar a string removendo duas chaves que está no começo e no final da string
        dados_string = dados_string.replace("'","")          # Tratar a string removendo as (') da string
        dados_string = dados_string.replace(" ","")          # Tratar a string removendo os espaços desnecessários
        
        dicionario = {}
        # Tratamento da string para dividir em tuplas
        for i in dados_string.split(","):
            my_tuplas = i.split(":")
            novo_elemento = {my_tuplas[0]: my_tuplas[1]}
            dicionario.update(novo_elemento)
        
        with open('dados_obtidos.csv', mode="a") as file:
            aux = str(dicionario["velocidade"]) + "," + str(dicionario["temperatura_motor"]) + "," + str(dicionario["pressao_pneu_dianteiro_esquerdo"]) + "," + str(dicionario["pressao_pneu_dianteiro_direito"]) + "," + str(dicionario["pressao_pneu_traseiro_esquerdo"]) + "," + str(dicionario["pressao_pneu_traseiro_direito"]) + "," + str(dicionario["rpm"]) + "," + str(dicionario["nivel_combustivel"]) + "," + str(dicionario["odometro"]) + "," + str(dicionario["status_farol"])
            file.write(aux)
            file.write("\n")

    
    else:
        print("mensagem não armazenada")
        client_socket.close()