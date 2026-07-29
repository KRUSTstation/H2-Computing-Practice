def readfile(filename):
    with open(f'./{filename}') as f:
        bytes = [i.strip() for i in f.readlines()]
    
    return bytes
	
	
def compress(bytes_list, bytes_pattern, byte_rep):
    pattern = []
    count = 0
    while count <= len(bytes_pattern) - 2:
        pattern.append(bytes_pattern[count:count+2])
        count+=2
    
    for i in range(len(bytes_list)):
        if i > len(bytes_list) - 1:
            break

        byte = bytes_list[i]

        if byte == pattern[0]:
            matched = True

            for j in range(1, len(pattern)):
                if pattern[j] != bytes_list[i+j]:
                    matched = False
                    break
            
            if matched:
                for j in range(len(pattern)):
                    bytes_list.pop(i)
                
                bytes_list.insert(i, byte_rep)

    return bytes_list
	

	
#main program
import socket 

print("-------------------")
print("SERVER OPEN")
print("-------------------")
print()

listen_socket = socket.socket() 
listen_socket.bind(('127.0.0.1', 9999)) 
listen_socket.listen()

print("Waiting for client request")
print("---------------------------")
new_socket, addr = listen_socket.accept()

original_lst = readfile("Audio.txt")
print(f"original data: {original_lst}")
print()

compressed_data = original_lst
keys = ""
#at least one compression must be done
while True:
        
    bytes_pattern = input("Enter the bytes pattern to be replaced: ") #636485, 6F2A6F, followed by 8385868788
    byte_rep = input("Enter the value to replace the above bytes pattern: ") #C0, C1 followed by C2
    compressed_data = compress(compressed_data, bytes_pattern, byte_rep)
    keys = keys + byte_rep + "," + bytes_pattern

    continue_input = input("Do you want to continue compressing? [Y/N]: ") 
    print()
    if continue_input == "N":
        break
    else:
        keys = keys + ","

print(f"compressed_data: {compressed_data}")
string_compressed_data = ''.join(compressed_data) #This is to convert the data from a list into a single string
encoded_compressed_data = string_compressed_data.encode() 
new_socket.sendall(encoded_compressed_data)
print(f"Compressed Data (String): {string_compressed_data}")
print("Compressed Data sent to client successfully")
print()

encoded_keys = keys.encode()
new_socket.sendall(encoded_keys)
print(f"Key: {keys}")
print("Key sent to client successfully")
print()

new_socket.close()

listen_socket.close()

print("-------------------")
print("SERVER CLOSED")
print("-------------------")
