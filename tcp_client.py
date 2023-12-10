import socket
import os

ServerName = 'localhost'
ServerPort = 12001

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ClientSocket.connect((ServerName, ServerPort))
except socket.error as err:
    print (f'Unable to connect to the server {err}')

ClientMessage = input('Please Enter Your Message\n')

ClientSocket.send(ClientMessage.encode())
ModifiedMessage = ClientSocket.recv(1024)
print (f'Response From Server:  {str(ModifiedMessage.decode())}')
ClientSocket.close()