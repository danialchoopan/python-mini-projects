import random
import os

list_food = []
while True:
    print("1-add food ")
    print("2-chose food ")
    print("3-show all food")
    print("4-remove food")
    print("0-exit ")
    user_input = int(input("select: "))
    if user_input == 1:
        food = input('enter the food: ')
        list_food.append(food)
        print('done')
    elif user_input == 2:
        if len(list_food) < 3:
            print('pls enter more food')
        else:
            list_len = len(list_food)-1
            result = list_food[
                random.randint(0, list_len)
            ]
            print(result)
        input('press any key for continue(a-z)')
    elif user_input == 3:
        for food in list_food:
            print(food)
        input('press any key for continue(a-z)')
    elif user_input==4:
        food=input('enter name food for remove: ')
        list_food.remove(food)
        for food in list_food:
            print(food)
        input('press any key for continue(a-z)')
    elif user_input == 0:
        break
    os.system("cls")
