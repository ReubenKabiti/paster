import os

def get_key_from_user():

    # use the terminal for now

    key = input("New user\nEnter API key (given to you when you create an account on pastebin): ")
    return key

def get_key():

    key = None

    if not os.path.exists("api.key"):
        key = get_key_from_user()
        with open("api.key", "w") as file:
            file.write(key)
    else:

        with open("api.key", "r") as file:
            key = file.read()

    return key


print(get_key())

