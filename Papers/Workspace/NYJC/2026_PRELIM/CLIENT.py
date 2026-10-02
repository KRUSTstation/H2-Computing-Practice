import socket

HOST = "127.0.0.1"
PORT = 65000

VALID_MOVES = ["UP", "DOWN", "LEFT", "RIGHT"]


def send_line(sock, message):
    sock.sendall((message + "\n").encode())     # Send message with newline as message boundary


client_socket = socket.socket()                 # Create client socket
client_socket.connect((HOST, PORT))             # Connect to server

buffer = ""                                     # Store received data until a full line is received

while True:
    while "\n" not in buffer:
        data = client_socket.recv(1024).decode()
        buffer += data

    message, buffer = buffer.split("\n", 1)     # Extract one complete line

    print(message)

    if message.startswith("GAME OVER"):
        break

    if message == "ENTER NAME":
        player_name = input("Enter your nickname: ")
        send_line(client_socket, player_name)

    elif message == "YOUR TURN":
        move = input("Enter move (UP/DOWN/LEFT/RIGHT): ").upper()

        while move not in VALID_MOVES:
            print("Invalid input. Please enter UP, DOWN, LEFT or RIGHT.")
            move = input("Enter move (UP/DOWN/LEFT/RIGHT): ").upper()

        send_line(client_socket, move)

client_socket.close()                           # Close client socket
