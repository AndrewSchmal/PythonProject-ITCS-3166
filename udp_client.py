import socket
import time

ServerName = '127.0.0.1'
ServerPort = 12003
SequenceNumber = 1

# Just for testing
print ("Running")

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while SequenceNumber <= 100:
    ClientSocket.sendto(f"msg {SequenceNumber}".encode(), (ServerName, ServerPort))
    SequenceNumber += 1