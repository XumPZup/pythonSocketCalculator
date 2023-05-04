import socket
 
 
def Main():
    # local host IP '127.0.0.1'
    host = input("Host: ")
    if host == '':
        host = "127.0.0.1"
 
    # Define the port on which you want to connect
    port = int(input("Port: "))
    if port == '':
        port = 12345
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # connect to server on local computer
    s.connect((host,port))
 
    # message you send to server
    message = "shaurya says geeksforgeeks"
    while True:
        message = input("Escreva 'q' para sair\nEscreva uma operaçao matematica:\n")
        # message sent to server
        if message == 'q':
            break
        s.send(message.encode("utf-8"))
 
        # message received from server
        data = s.recv(1024)
 
        # print the received message
        # here it would be a reverse of sent message
        print('Resposta: ',str(data.decode("utf-8")))
 
    # close the connection
    s.close()
 
if __name__ == '__main__':
    Main()