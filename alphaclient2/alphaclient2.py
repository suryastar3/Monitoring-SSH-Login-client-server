import socket
import tailer

def client_program():
    host = '192.168.0.140'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    init_attempt = 0
    for line in tailer.follow(open('/var/log/auth.log')):
        if 'password' in line:
            login_attempt = init_attempt + 1
            message = ("NodeXYZ had " + str(login_attempt) + " attempt of ssh login")
            client_socket.send(message.encode())
            init_attempt = login_attempt

    client_socket.close()

if __name__ == '__main__':
    client_program()
