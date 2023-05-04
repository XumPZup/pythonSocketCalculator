import socket
from _thread import *
import threading
 

print_lock = threading.Lock()


def validade_message(message):
    # There must be no alphabetic characters
    for c in message:
        if c.isalpha():
            return False
    try:
        value = eval(message)
        return value
    except SyntaxError:
        return False

 
# thread function
def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Thread fechado')
             
            # lock released on exit
            print_lock.release()
            break
 
        # validade operation
        is_valid = validade_message(data.decode('utf-8'))
        # send back answer
        if is_valid:
            message = str(is_valid)
        else:
            message = "Operaçao nao valida!"

        c.send(message.encode("utf-8"))
    # connection closed
    c.close()

 
def Main():
    host = ""
 
    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket conectado na porta", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket escutando")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()