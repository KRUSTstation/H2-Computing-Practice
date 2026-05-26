def encrypt(plaintext):
    #copy and paste your encrypt function here
	

#main program
import socket

print("-------------------")
print("CLIENT OPEN")
print("-------------------")
print()

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 9999))

message = input("Enter message: ")
encrypted_message = encrypt(message)

data = encrypted_message.encode()
my_socket.sendall(data + b'\n')
print("message sent")
my_socket.close()

print("-------------------")
print("CLIENT CLOSED")
print("-------------------")
