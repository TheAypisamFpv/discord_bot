import requests  # dependency

global mentions
mentions = {
    "@Myself": "<@390466864356130817>",
    "@everyone": "<@&1034789618626854972>",
    "@Admins": "<@&1034789794422726726>"
}

print('\nMentions:')
for mention in mentions:
    print('-',mention)

def send_mess():
    # webhook url, from here: https://i.imgur.com/f9XnAew.png
    URL_info = "https://discord.com/api/webhooks/1115187961764511784/2CCWWVOaG86ZZxeo0EejO-qAc1jVekCFwxNVlhjGy_WmfU9kBu5CR70mpTvWxVFKci7V"
    URL_general = "https://discord.com/api/webhooks/1113755918459482113/J_YJ_KnN2GYcPiHQsBpAbwoyh6wFdycmwOzCaD4_tshy-75sI7N4tDF4gJc2LjuKoctX"

    content = input('\nsimple message: ')
    title = input('Embed Title: ')
    description = input('Embed description: ')
    username = input('username: ')

    fullmess = [content, description, title]

    for mess in range(len(fullmess)):
        # print('mess', fullmess[mess])
        for mention in mentions:
            # print('mention', mention)
            if mention in fullmess[mess]:
                # print('Yousk2')
                fullmess[mess] = fullmess[mess].replace(mention, mentions[mention])

    data = {
        "content": fullmess[0],
        "embeds": [
            {
                "type": "rich",
                "title": fullmess[2],
                "description": ''+fullmess[1],
                "color": 0xFBE214
            }
        ],
        "footer": {
            "text": "-Detroit become human"
        },
        "username": username
    }

    print(fullmess)


    result = requests.post(URL_info, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.\n".format(result.status_code))



send_mess()