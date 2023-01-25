import requests  # dependency

# webhook url, from here: https://i.imgur.com/f9XnAew.png
url = "https://discord.com/api/webhooks/1067913290761654404/biC9E1gE6AIMs0TRCLXiOmAERYoJL3F6bLXyXXk_0vuOC8iza4n363m2zdTy404FQemh"


while True:
    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content": '<@&1067546567105589358>',
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