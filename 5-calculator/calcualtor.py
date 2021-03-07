import os
while True:
    os.system('cls')
    print('welecome to calculator app')
    number_1 = float(input('enter number 1: '))
    number_2 = float(input('enter number 2: '))
    os.system('cls')
    print('{} ? {}'.format(number_1, number_2))
    print('1- + ')
    print('2- - ')
    print('3- * ')
    print('4- / ')
    print('0-exit')
    user_input = int(input('select : '))
    if user_input == 1:
        result = number_1+number_2
        print('{} + {} = {}'.format(number_1, number_2, result))
    elif user_input == 2:
        result = number_1-number_2
        print('{} - {} = {}'.format(number_1, number_2, result))
    elif user_input == 3:
        result = number_1*number_2
        print('{} * {} = {}'.format(number_1, number_2, result))
    elif user_input == 4:
        result = number_1/number_2
        print('{} / {} = {}'.format(number_1, number_2, result))
    input('press enter')
