def generateKey(key, string):
    pass
    # Fill in code here

    
def encrypt(password, message):
    pass
    # Fill in code here



def decrypt(password, message):
    pass
    # Fill in code here


# Client program

import socket


print("Please set a password.")
password = input("Answer:")
print()
print("What is your Team Name?")
name = input("Answer:")
print()
print("Group size?")
size = input("Answer:")
print()

encry_key = password

items = [password,size,name]
for i in range(len(items)):
    items[i] = encrypt(encry_key, items[i])

message = "/".join(items)

print("Establishing connection...")
s = socket.socket()
s.connect(('127.0.0.1', 9999))
print("Connection established!")

data = b''

s.sendall(message.encode() + b'\n')
print("Data sent!")

print()
print("Waiting for the server to confirm your request...")
print()
data=s.recv(1024)

decrypted_data = data
decrypted_data = decrypted_data.decode()

decrypted_data = decrypt(password,decrypted_data)      

if decrypted_data=="cancelled":
    print("""Pickup cancelled. 
Wrong password or request rejected.
Please try again.""")

if decrypted_data=="confirmed":
    print("""Pickup confirmed! Please wait for pickup to arrive.""")

s.close()
print()
print("Connection disconnected.")
