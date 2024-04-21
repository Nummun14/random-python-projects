player1name = input("player1, what's your name?")
player2name = input("player2, what's your name?")
num = 1
boom = "boom"

while True:
    player1 = input(player1name)
    if num % 7 == 0:
        if player1 != boom:
            print(player1name, "lost")
            exit()
    elif num % 10 == 7:
        if player1 != boom:
            print(player1name, "lost")
            exit()
    elif player1 == boom:
        print(player1name, "lost")
        exit()
    elif int(player1) != num:
        print(player1name, "lost")
        exit()
    num = num + 1

    player2 = input(player2name)
    if num % 7 == 0:
        if player2 != boom:
            print(player2name, "lost")
            exit()
    elif num % 10 == 7:
        if player2 != boom:
            print(player2name, "lost")
            exit()
    elif player2 == boom:
        print(player2name, "lost")
        exit()
    elif int(player2) != num:
        print(player2name, "lost")
        exit()
    num = num + 1
