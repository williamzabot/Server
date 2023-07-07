from socket import *
from CustomPing import *

# no servidor é utilizada a connection para enviar uma mensagem para o cliente
# enquanto no cliente é utilizado o socketServer
myHost = 'localhost'
myPort = 50001
socketServer = socket(AF_INET, SOCK_STREAM)
socketServer.bind((myHost, myPort))
socketServer.listen(1)
print("Servidor na escuta...")
connection, address = socketServer.accept()
print('Server connected: ', connection)
while True:
    url = connection.recv(1024).decode("utf-8")
    if url == ":q":
        connection.close()
        break
    ping = str(doPing(url))
    connection.send(ping.encode("utf-8"))



