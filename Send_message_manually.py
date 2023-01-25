import requests  # dependency

# webhook url, from here: https://i.imgur.com/f9XnAew.png
url = "https://discord.com/api/webhooks/1067802730833395824/qqCfC3H3BmOIAMe5qwy15rTuxjlsOSSUpZY8iXac7VE9w-7r2RU7V-05KxoAYPOnlqFc"


while True:
    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content": '<@&1067548245863186472>',
        "embeds": [
            {
                "type": "rich",
                "description": "<@390466864356130817> est un incompétant",
                "title": "ceci est un test de @",
                "color": 0xFBE214
            }
        ],
        "footer": {
            "text": "-Detroit become human"
        }
        # "username" : input('username: ')
    }

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.\n".format(result.status_code))

    
    break