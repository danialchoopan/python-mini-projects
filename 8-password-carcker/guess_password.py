import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    for i in range(1, 9):
        for guess in itertools.product(chars, repeat=i):
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}.'.format(guess)
                break
            print(guess)

print(guess_password('1234'))
