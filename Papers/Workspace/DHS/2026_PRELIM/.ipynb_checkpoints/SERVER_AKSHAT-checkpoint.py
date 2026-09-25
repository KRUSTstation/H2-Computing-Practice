# Task 3.2
from socket import socket
import sqlite3
from random import sample

s = socket()

s.bind(('', 6789))

s.listen()

conn = sqlite3.connect('minesweeper.db')
cursor = conn.cursor()

with conn:
    cursor.execute('SELECT xCoordinate, yCoordinate FROM Board')
    board = cursor.fetchall()

    for tile in board:
        cursor.execute('DELETE FROM Board WHERE xCoordinate = ? AND yCoordinate = ?', tile)

    mines = sample([i for i in range(1, 17)], 10)

    tile_no = 1
    for x in range(1, 5):
        for y in range(1, 5):
            if tile_no in mines:
                is_mine = 1
            else:
                is_mine = 0
            
            cursor.execute('INSERT INTO Board VALUES (?, ?, ?, ?)', (x, y, is_mine, 0))

            tile_no += 1

    conn.commit()
    
    s.listen()
    c, addr = s.accept()

    checked = 0
    while checked < 6:
        coords = c.recv(4096).decode()
        x, y = [int(i) for i in coords.split(',')]

        cursor.execute('UPDATE Board SET checked = 1 WHERE xCoordinate = ? AND yCoordinate = ?', (x, y))
        conn.commit()
        
        cursor.execute('SELECT hasMine FROM Board WHERE xCoordinate = ? AND yCoordinate = ?', (x, y))
        is_mine = cursor.fetchone()[0]

        if is_mine == 1:
            c.send('MINE'.encode())
            print('MINE HIT!')
            break
        else:
            cursor.execute('SELECT Count(checked) FROM Board')
            checked = cursor.fetchone()[0]

            surrounding_mines = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0: continue
                    
                    x_offset = x + i
                    y_offset = y + j

                    cursor.execute('SELECT hasMine FROM Board WHERE xCoordinate = ? AND yCoordinate = ?', (x_offset, y_offset))
                    is_mine = cursor.fetchone()[0]

                    if is_mine == 1:
                        surrounding_mines += 1

            c.send(f'{surrounding_mines},{checked}'.encode())