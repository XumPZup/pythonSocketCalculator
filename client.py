import socket
 
 
def Main():
    # Define host IP ('127.0.0.1')
    host = input("Host: ")
    
    # Define the port on which you want to connect (12345)
    port = int(input("Port: "))
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    # Connect to server
    s.connect((host,port))
 
    while True:
        # User message
        message = input("Escreva 'q' para sair\nEscreva uma expressão matemática:\n")
        # message sent to server
        if message == 'q':
            break

        s.send(message.encode("utf-8"))
        # message received from server
        data = s.recv(1024)
        # Print the response
        print('Resposta: ',str(data.decode("utf-8")))
 
    # close the connection
    s.close()
 
if __name__ == '__main__':
    Main()