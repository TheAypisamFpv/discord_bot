from arrow import get
import requests, get_credentials

URL_info = get_credentials.URL_info()

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
