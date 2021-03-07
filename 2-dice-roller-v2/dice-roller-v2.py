import random
import os

while True:
    os.system('cls')
    print('dice roller v2 :-)')
    print('1-roll the dice')
    print('0-exit')
    user_input = int(input('select: '))
    if user_input == 1:
        random_number = random.randint(1, 6)
        if random_number == 1:
            print('-----------')
            print('|         |')
            print('|    0    |')
            print('|         |')
            print('-----------')
        elif random_number == 2:
            print('-----------')
            print('|         |')
            print('|  0   0  |')
            print('|         |')
            print('-----------')
        elif random_number == 3:
            print('-----------')
            print('|         |')
            print('| 0  0  0 |')
            print('|         |')
            print('-----------')
        elif random_number == 4:
            print('-----------')
            print('|  0    0 |')
            print('|         |')
            print('|  0    0 |')
            print('-----------')
        elif random_number == 5:
            print('-----------')
            print('|  0    0 |')
            print('|     0   |')
            print('|  0    0 |')
            print('-----------')
        elif random_number == 6:
            print('-----------')
            print('| 0  0  0 |')
            print('|         |')
            print('| 0  0  0 |')
            print('-----------')
        input('')
    elif user_input==2:
        break

