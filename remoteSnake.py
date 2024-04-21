import socket
import keyboard

HOST = ''
PORT = 0000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
inp = 'a'
while True:
    if keyboard.is_pressed('w') == True:
        inp = 'w'
        socket.send(inp.encode('utf-8'))
        print(socket.recv(1024).decode('utf-8'))

    if keyboard.is_pressed('s') == True:
        inp = 's'
        socket.send(inp.encode('utf-8'))
        print(socket.recv(1024).decode('utf-8'))


    if keyboard.is_pressed('d') == True:
        inp = 'd'
        socket.send(inp.encode('utf-8'))
        print(socket.recv(1024).decode('utf-8'))

    if keyboard.is_pressed('a') == True:
        inp = 'a'
        socket.send(inp.encode('utf-8'))
        print(socket.recv(1024).decode('utf-8'))