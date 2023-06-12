import requests

URL_info = "https://discord.com/api/webhooks/1115187961764511784/2CCWWVOaG86ZZxeo0EejO-qAc1jVekCFwxNVlhjGy_WmfU9kBu5CR70mpTvWxVFKci7V"

def send_alert():
    message = ":warning: <@&1067743463174582343> __***Contrôle de présence***__ :warning:"
    data = {
        "content": message,
        "attachments": []
    }
    try:
        requests.post(URL_info, json=data)
    except Exception as e:
        print(e)

send_alert()