import math


powers = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}




def last_digit(n1, n2):
    if n2 == 0:
        return 1
    last_digit_of_base = n1
    if n1 >= 10:
        last_digit_of_base = n1 % 10
    cycle = len(powers[last_digit_of_base])
    mod_cycle = n2 % cycle
    if mod_cycle == 0:
        return powers[last_digit_of_base][cycle - 1]
    return powers[last_digit_of_base][mod_cycle - 1]


print(last_digit(4, 1))
print(last_digit(4, 2))
print(last_digit(9, 7))
print(last_digit(10, 10 ** 10))
print(last_digit(2 ** 200, 2 ** 300))
print(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651)
