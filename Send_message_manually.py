import requests, get_credentials

URL_info = get_credentials.URL_info()
URL_general = get_credentials.URL_general()


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
    "embeds": 
    [
      {
        "type": "rich",
        "title": fullmess[2],
        "description": ''+fullmess[1],
        "color": 0xFBE214
      }
    ]
    ,"footer": 
    {
      "text": "-Detroit become human"
    }
    ,"username": username
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