from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET=tipo de identificacao com meu servidor
obj_socket.bind((servidor, porta))
obj_socket.listen(2)  # quantidade de clientes maximas que a aplicacao podera escutar/receber uma conexao

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))  # maximo que posso receber é 1024 bytes
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Ola cliente'
        con.send(msg_enviada)
        break
    con.close()
