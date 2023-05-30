import os
import requests

API_ENDPOINT = "https://pastebin.com/api/api_post.php"

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


def main():

    key = get_key()

    while True:

        paste = ""

        print("Enter paste, \\n to finish paste\n")

        while True:
            p = input()
            if p == "\n":
                break
            paste += p


        paste_name = input("Name of paste []: ")

        paste_format = input("Format of paste [php]: ")
        if not paste_format:
            paste_format = "php"


        paste_privacy = input("Privacy 0 - public, 1 - unlisted, 2 - private [0]: ")
        if not paste_privacy:
            paste_privacy = "0"

        payload = {
                "api_dev_key": key,
                "api_option": "paste",
                "api_paste_code": paste,
                "api_paste_name": paste_name,
                "api_paste_format": paste_format,
                "api_paste_private": paste_privacy,
        }

        r = request.post(url=API_ENDPOINT, data=payload)
        url = r.text
        print(f"\nPastebin url = {url}\n")



if __name__ == "__main__":
    main()
