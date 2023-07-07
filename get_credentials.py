def get_all():
  with open("credential.txt", "r") as f:
    data = [line.partition("=")[-1].strip() for line in f.readlines()]
  return data

def URL_agenda():
  return get_all()[0]

def URL_english():
  return [get_all()[1], get_all()[2]]

def URL_info():
  return get_all()[3]

def URL_ent():
  return get_all()[4]

def URL_ent_redirect():
  return get_all()[5]

def USERNAME():
  return get_all()[6]

def PASSWORD():
  return get_all()[7]

def URL_general():
  return get_all()[8]
