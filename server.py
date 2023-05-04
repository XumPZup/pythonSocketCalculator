import socket
from _thread import *
import threading
 

print_lock = threading.Lock()


# Validate expression
def validade_message(message):
    # There must be no alphabetic characters
    for c in message:
        if c.isalpha():
            return False
    try:
        # Try to evaluate
        value = eval(message)
        return value
    except SyntaxError:
        # Evaluation failed
        return False

 
# thread function
def threaded(c):
    while True:
        # Data received from client
        data = c.recv(1024)
        if not data:
            print('Thread fechado')
            # Lock released on exit
            print_lock.release()
            break
        # Validade expression
        is_valid = validade_message(data.decode('utf-8'))
        if is_valid:
            message = str(is_valid)
        else:
            message = "Expressão inválida!"
        # Send answer
        c.send(message.encode("utf-8"))
    # Close connection
    c.close()

 
def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Socket conectado na porta", port)
    # Put the socket into listening mode
    s.listen(5)
    print("Socket escutando")
    while True:
        # Establish connection with client
        c, addr = s.accept()
        # Lock acquired by client
        print_lock.acquire()
        print(f'Connectado a : {addr[0]}:{addr[1]}')
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()