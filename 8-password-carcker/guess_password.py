import itertools
import string

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    while True:
        for guess in itertools.product(chars):
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}.'.format(guess)
                break
            print(guess)

print(guess_password('1234567890'))