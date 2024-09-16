import random

playing = True
card = 0
player = []
John = []
Mark = []
Janet = []
Sarah = []
players = [player, John, Mark, Janet, Sarah]

# Define the deck of cards
deck = [('Ace', 'Hearts'), ('2', 'Hearts'), ('3', 'Hearts'), ('4', 'Hearts'),
        ('5', 'Hearts'), ('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'),
        ('9', 'Hearts'), ('10', 'Hearts'), ('Jack', 'Hearts'), ('Queen', 'Hearts'),
        ('King', 'Hearts'), ('Ace', 'Diamonds'), ('2', 'Diamonds'), ('3', 'Diamonds'),
        ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'), ('7', 'Diamonds'),
        ('8', 'Diamonds'), ('9', 'Diamonds'), ('10', 'Diamonds'), ('Jack', 'Diamonds'),
        ('Queen', 'Diamonds'), ('King', 'Diamonds'), ('Ace', 'Clubs'), ('2', 'Clubs'),
        ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'), ('7', 'Clubs'),
        ('8', 'Clubs'), ('9', 'Clubs'), ('10', 'Clubs'), ('Jack', 'Clubs'), ('Queen', 'Clubs'),
        ('King', 'Clubs'), ('Ace', 'Spades'), ('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'),
        ('5', 'Spades'), ('6', 'Spades'), ('7', 'Spades'), ('8', 'Spades'), ('9', 'Spades'),
        ('10', 'Spades'), ('Jack', 'Spades'), ('Queen', 'Spades'), ('King', 'Spades'),
        ('Joker', 'Black'), ('Joker', 'White')]

random.shuffle(deck)
random.shuffle(players)

for i in range(10):
    for person in players:
        person.append(deck[card])
        card += 1
players[0].append(deck[card])
card += 1
players[1].append(deck[card])
card += 1
players[3].append(deck[card])
card += 1
players[4].append(deck[card])
card += 1

for start in players:
    if ('3', 'Clubs') in start:
        players.remove(start)
        players.insert(0, start)

while playing:
    for turn in players:
        if turn == player:
            print(player)
            placed = input("what do you want to play?")
            tuple(placed.split())
            print(placed)
            player.remove(placed)


