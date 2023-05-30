import os
import requests

API_ENDPOINT = "https://pastebin.com/api/api_post.php"

ERRORS = [
"Bad API request, invalid api_option",
"Bad API request, invalid api_dev_key",
"Bad API request, maximum number of 25 unlisted pastes for your free account",
"Bad API request, maximum number of 10 private pastes for your free account",
"Bad API request, api_paste_code was empty",
"Bad API request, maximum paste file size exceeded",
"Bad API request, invalid api_paste_expire_date",
"Bad API request, invalid api_paste_private",
"Bad API request, invalid api_paste_format",
"Bad API request, invalid api_user_key",
"Bad API request, invalid or expired api_user_key",
"Bad API request, you can't add paste to folder as guest",
]

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


    paste = ""

    print("Enter paste, \\n to finish paste\n")

    while True:
        p = input()
        if p == "\\n":
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

    r = requests.post(url=API_ENDPOINT, data=payload)
    url = r.text
    if url in ERRORS:
        print(f"There was an error: {url}")

    print(f"\nPastebin url = {url}\n")



if __name__ == "__main__":
    main()
