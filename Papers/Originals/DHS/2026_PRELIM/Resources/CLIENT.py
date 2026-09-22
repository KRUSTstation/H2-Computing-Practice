import socket

print("-------------------------")
print("MINESWEEPER GAME [CLIENT]")
print("-------------------------")
print()

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 6789))

while True:

    print("Select your coordinate:")
    chosen_xCoord = input("INPUT x Coordinate: ")
    chosen_yCoord = input("INPUT y Coordinate: ")
    print()

    coordinates = chosen_xCoord + "," + chosen_yCoord
    my_socket.sendall(coordinates.encode())

    response = my_socket.recv(1024).decode()

    if response == 'MINE':
        print("You have hit a mine! You lose!")
        break
    else:  
        no_of_surrounding_mines, no_of_coordinates_checked = response.split(",")
        
        print("Great job! You did not hit a mine!")

        if int(no_of_coordinates_checked) == 6:
            print("You have found all the coordinates without mine. You win!")
            break
        else:
            print(f"There are {no_of_surrounding_mines} mine(s) around your last selected coordinate and you have checked {no_of_coordinates_checked} coordinate(s)!")
            print()
    


my_socket.close() 

print("-------------------")
print("GAME ENDED")
print("-------------------")
