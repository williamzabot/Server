from socket import *
from CustomPing import *
from User import User

file = "ls.txt"
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
2 - Logar
3 - ls""")
        clientMsg = receive()
        if clientMsg == ":q":
            connection.close()
            print("encerrando..")
            break
        elif clientMsg == "1":
            user = User()
            send("Digite o username: ")
            user.username = receive()
            send("Digite a senha: ")
            user.password = receive()
            users.append(user)
            print(f"{user.username} adicionado!")
        elif clientMsg == "2":
            send("Digite o username: ")
            username = receive()
            send("Digite a senha: ")
            password = receive()
            userExist = False
            for userDoArray in users:
                if userDoArray.username == username:
                    if userDoArray.password == password:
                        userExist = True
                        send("Logado com sucesso! Digite uma url ")
                        url = receive()
                        ping = str(doPing(url))
                        #send(ping)
                        print(ping)
            if not userExist:
                print("Usuário inválido")
        elif clientMsg == "3":
            command = f"ls > {file}"
            os.system(command)
            arq = open(file)
            directories = ""
            lines = arq.readlines()
            for line in lines:
                directories += line
            #send(directories)
            print(directories)
        else:
            print("escolha inválida")

menu()