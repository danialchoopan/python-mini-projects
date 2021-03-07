import random

while True:
    print('welecome to dice roller app')
    print('1-roll the dice')
    print('2-exit')
    user_input = int(input('select : '))
    if user_input == 1:
        print("roll : ", random.randint(1, 6))
    elif user_input == 2:
        break
