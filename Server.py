from socket import *
from CustomPing import *
from User import User

users = []

myHost = 'localhost'
myPort = 1024
socketServer = socket(AF_INET, SOCK_STREAM)
socketServer.bind((myHost, myPort))
socketServer.listen(1)
print("Servidor na escuta...")
connection, address = socketServer.accept()
def receive():
    return str(connection.recv(1024).decode("utf-8"))

def send(message):
    connection.send(message.encode("utf-8"))
def menu():
    while True:
        send("""
1 - Registrar usuário 
2 - Logar""")
        clientMsg = receive()
        if clientMsg == ":q":
            connection.close()
            break
        elif clientMsg == "1":
            user = User()
            send("Digite o username: ")
            user.username = receive()
            send("Digite a senha: ")
            user.password = receive()
            users.append(user)
        elif clientMsg == "2":
            send("Digite o username: ")
            username = receive()
            send("Digite a senha: ")
            password = receive()
            for userDoArray in users:
                if userDoArray.username == username:
                    if userDoArray.password == password:
                        send("Logado com sucesso! Digite uma url ")
                        url = receive()
                        ping = str(doPing(url))
                        send(ping)
        else:
            print("escolha inválida")

menu()