import datetime
import json
import locale
import time

import keyboard
import requests
from bs4 import BeautifulSoup
from webbot import Browser

locale.setlocale(locale.LC_TIME, 'fr_FR')

debug_ = True

post_ = True


# https://discord.com/api/v9/channels/1038800615494656141/messages/1039230514202153021

# ID_message = ["https://discord.com/channels/1017438249494519948/1038800615494656141/1039230514202153021",
#               "https://discord.com/channels/1017438249494519948/1038800615494656141/1039230516710350918",
#               "https://discord.com/channels/1017438249494519948/1038800615494656141/1039230520279695473",
#               "https://discord.com/channels/1017438249494519948/1038800615494656141/1039230523991654561",
#               "https://discord.com/channels/1017438249494519948/1038800615494656141/1039230528282443826",
#               "https://discord.com/channels/1017438249494519948/1038800615494656141/1039230532820684851"
# ]


if debug_:
    print('')

response_ = []

null = None
false = False

url_bot = "https://discord.com/api/webhooks/1036402415383101481/glx28oB9Ug5CdABtutn9_cNclkjdsxA9sER_hp2m6YCKtCVeT65iiJNqNt4ZLn4m5DaQ"
url = "https://wayf.cesi.fr/login?service=https%3A%2F%2Fent.cesi.fr%2Fservlet%2Fcom.jsbsoft.jtf.core.SG%3FPROC%3DIDENTIFICATION_FRONT"
url_redirect = "https://sts.viacesi.fr/adfs/ls/?UserName=samuel.courtin@viacesi.fr"
username = 'samuel.courtin@viacesi.fr'
password = 'HRBbESMTq78chNr4qh9i8pxREftyG'

today = datetime.date.today()
if today.weekday() == 5 or today.weekday() == 6:
    start_week = today + datetime.timedelta(days= 7 - today.weekday())
else:
    start_week = today - datetime.timedelta(days=today.weekday())

end_week = start_week + datetime.timedelta(days=6)

timezone = str(":00+0" + str(time.localtime().tm_hour - time.gmtime().tm_hour))
if debug_:
    print(today.strftime("%d/%m/%Y"), timezone)
    print(start_week.strftime("%d/%m/%Y"), end_week.strftime("%d/%m/%Y"))


def get_cours(_calendar_url_):
    response_ = ""
    web = Browser()

    web.go_to(url)

    web.type(username, into='login', id='login')
    web.click('Valider', id='submit')

    web.type(password, into='Password', id='passwordInput')
    web.click('Connexion', id='submitButton')

    web.go_to(_calendar_url_)
    request_code = requests.get(_calendar_url_).status_code

    # if request_code != requests.codes.ok:
    #     print(f"\nError {request_code}")
    #     send_email(request_code, _calendar_url_, web)

    #     return response_, False

    if debug_:
        print("good url")

    content = web.get_page_source()
    response_ = BeautifulSoup(content, features="html.parser").get_text()
    response_ = json.loads(response_)
    if debug_:
        print(response_.__class__)
        print(response_)
    return response_, True


def updatebot(response_):

    data = {
        "content": "",
        "username": "Bot agenda",
        "message_reference": {
            "message_id": "",
            "fail_if_not_exists": True
        },
        "embeds": [{
            "type": "rich",
            "description": " ",
            "title": " ",
            "color": 0xdddddd,
            "fields": [{
                "name": "",
                "value": "\u200B"
                }]
            }
        ],
        "footer": {
            "text": "",
            "icon_url": ""
        }
    }

    Lundi = ""
    Mardi = ""
    Mercredi = ""
    Jeudi = ""
    Vendredi = ""
    day = [Lundi, Mardi, Mercredi, Jeudi, Vendredi]


    day_change = []

    for i in range(len(response_)-1):
        if response_[i]["start"].partition("T")[0] != response_[int(i+1)]["start"].partition("T")[0]:
            day_change.append(i+1)
    day_change.append(len(response_)+1 )


    div = ""
    for h in range(len(response_)):
        if h == day_change[d]:
            d = d+1
            div = ""
        title = str(response_[h]["title"]) + '\n'
        hour = str(response_[h]["start"].partition("T")[2].removesuffix(timezone)) + " - " + str(response_[h]["end"].partition("T")[2].removesuffix(timezone)) + '\n\n'

        if title == "Anglais\n":
            title = "Anglais (en fonction de votre groupe)\n"
            hour = '13:30 - 16:30 \n'
        if title == "Soutenance - Exposé\n":
            title = "Soutenance - Exposé (en fonction de votre groupe)\n"
        div = div + title + hour
        day[d] = div
        


    for i in range(len(day)):
        if day[i] == "":
            day[i] = "jour férié"


    for d in range(-1,len(day)):  

        if d == -1:
            data["embeds"] = [
                {
                    "type": "rich",
                    "title": "Emploi du temps de la semaine n°{} ({} - {}) :".format(start_week.isocalendar().week, start_week.strftime("%d/%m/%Y"), end_week.strftime("%d/%m/%Y")),
                    "color": 0xFBE214,
                    # "url": ID_message[d]
                    }
                ]
        elif d >= 0:
            data["embeds"] = [
                {
                    "type": "rich",
                    "description": "",
                    "title": "__"+( start_week + datetime.timedelta(days=d) ).strftime("%A %d %B")+"__",
                    "color": 0xDDDDDD,
                    # "url": ID_message[d],
                    "fields": [
                        {
                            "name": day[d],
                            "value": "\u200B"
                        }
                    ],
                }
            ]
        if d == 4:
            data["footer"] = {
                "text": "source: https://ent.cesi.fr/api/seance/",
                "icon_url": "https://yt3.ggpht.com/ytc/AMLnZu-r9SK3rtCm-hF3UlW1nolyr8mIBJS10FBnIKFDHw=s900-c-k-c0x00ffffff-no-rj"
                }


        if debug_:
            print(data["embeds"],'\n')

        if post_:
            result = requests.post(url_bot, json=data)
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print("--ERROR--  ", err)
            else:
                if debug_:
                    print("Payload delivered successfully, code {}.".format(result.status_code))
                    print(d)
        else:
            print("--ERROR--  post_ is set to {}".format(post_))
            
        d+1


def send_email(error_code: int, url: str, web) -> None:
    return 
    mdp = 'HRBbESMTq78chNr4qh9i8pxREftyG'
    user = 'samuel.courtin@viacesi.fr'
    to = 'the.aypisam.64@gmail.com'

    print("envoie de l'email...")

    message = f"Ceci est un message automatique.\n----------\nConnexion à l'url '{url}' s'est terminé par un code d'erreur {error_code}\n----------\n\n-Detroit Become Human"

    print(message)
    web.go_to('https://outlook.office.com/')

    web.type(user)
    keyboard.press_and_release('enter')
    time.sleep(1)

    web.type(mdp)
    keyboard.press_and_release('enter')
    time.sleep(200)
    # keyboard.press_and_release('tab')
    # keyboard.press_and_release('tab')
    # keyboard.press_and_release('tab')
    # keyboard.press_and_release('enter')
    # time.sleep(1)
    web.go_to('https://outlook.office.com/compose')
    time.sleep(5)
    keyboard.write(to)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.write('Connexion impossible')
    keyboard.press_and_release('tab')
    keyboard.write(message)
    keyboard.press_and_release('enter')

    pass





def main():
    calendar_url = 'https://ent.cesi.fr/api/seance/all?start={}&end={}&codePersonne=2427950&_=1665606186346'.format(start_week, end_week)
    if debug_:
        print(calendar_url)
    response_, is_good = get_cours(calendar_url)
    if is_good == True:
        updatebot(response_)
        if debug_:
            print("bonne chance pour cette semaine")

    if debug_:
        print('')



main()
