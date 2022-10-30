import requests
import time



url = "********************************"


data = {
    "content": "",
    "username": "Bot agenda",
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
    "footer":{
        "text": "",
        "icon_url": ""
    }
}


null = None
false = False

# response_ = [
#     {
#         "code":"4090524",
#         "title":"Travail de groupe",
#         "allDay":false,
#         "nightly":false,
#         "start":"2022-10-28T09:00:00+02",
#         "end":"2022-10-28T12:30:00+02",
#         "url":"",
#         "nomModule":"",
#         "matiere":null,
#         "theme":"",
#         "salles":[
#             {
#                 "nomSalle":"N102"
#             },
#             {
#                 "nomSalle":"N104A CPI A2"
#             },
#             {
#                 "nomSalle":"N104B CPI A2"
#             }
#         ],
#         "intervenants":[
#             {
#                 "sousTitre":null,
#                 "profils":null,
#                 "groupesPedagogiques":null,
#                 "urlFiche":"https://ent.cesi.fr/servlet/urlfiche?OBJET=PERSONNE&CODE=1228634&LANGUE=0",
#                 "urlPhoto":"https://ent.cesi.fr/images/fo/avatar-homme.jpg",
#                 "nom":"AMAMOU",
#                 "prenom":"Mohamed",
#                 "code":"1228634",
#                 "adresseMail":"",
#                 "urlAgenda":"",
#                 "sessions":[],
#                 "inconnu":false
#             }
#         ],
#         "participantsPersonne":null,
#         "participants":[
#             {
#                 "libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète",
#                 "codeGroupe":"155923",
#                 "codeSession":"2182217"
#             }
#         ]
#     },
#     {
#         "code":"4107205",
#         "title":"Prosit aller",
#         "allDay":false,
#         "nightly":false,
#         "start":"2022-10-28T13:30:00+02",
#         "end":"2022-10-28T15:00:00+02",
#         "url":"",
#         "nomModule":"",
#         "matiere":null,
#         "theme":"",
#         "salles":[
#             {
#                 "nomSalle":"N102"
#             }
#         ],
#         "intervenants":[
#             {
#                 "sousTitre":null,
#                 "profils":null,
#                 "groupesPedagogiques":null,
#                 "urlFiche":"https://ent.cesi.fr/servlet/urlfiche?OBJET=PERSONNE&CODE=2430574&LANGUE=0",
#                 "urlPhoto":"https://ent.cesi.fr/images/fo/avatar-homme.jpg",
#                 "nom":"MAHIEU",
#                 "prenom":"Romain",
#                 "code":"2430574",
#                 "adresseMail":"",
#                 "urlAgenda":"",
#                 "sessions":[],
#                 "inconnu":false
#             }
#         ],
#         "participantsPersonne":null,
#         "participants":[
#             {
#                 "libelleGroupe":"CPI A1 22-23 Rouen - Bloc Electronique - Groupe Romain - N 102",
#                 "codeGroupe":"182358","codeSession":"2182217"
#             }
#         ]
#     },
#     {
#         "code":"4107209",
#         "title":"Travail de groupe",
#         "allDay":false,
#         "nightly":false,
#         "start":"2022-10-28T15:00:00+02",
#         "end":"2022-10-28T16:00:00+02",
#         "url":"",
#         "nomModule":"",
#         "matiere":null,
#         "theme":"",
#         "salles":[
#             {
#                 "nomSalle":"N102"
#             }
#         ],
#         "intervenants":null,
#         "participantsPersonne":null,
#         "participants":[
#             {
#                 "libelleGroupe":"CPI A1 22-23 Rouen - Bloc Electronique - Groupe Romain - N 102",
#                 "codeGroupe":"182358",
#                 "codeSession":"2182217"
#             }
#         ]
#     }
# ]


response_ = [
    {
        "code":"4019671",
        "title":"A planifier",
        "allDay":false,
        "nightly":false,
        "start":"2022-11-07T09:30:00+01",
        "end":"2022-11-07T12:30:00+01",
        "url":"",
        "nomModule":"",
        "matiere":null,
        "theme":"",
        "salles":[
            {
                "nomSalle":"N102"
            },
            {
                "nomSalle":"N104A CPI A2"
            },
            {
                "nomSalle":"N104B CPI A2"
            }
        ],
        "intervenants":null,
        "participantsPersonne":null,
        "participants":[
            {
                "libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète",
                "codeGroupe":"155923",
                "codeSession":"2182217"
            }
        ]
    },
    {
        "code":"4019672",
        "title":"A planifier",
        "allDay":false,
        "nightly":false,
        "start":"2022-11-07T13:30:00+01",
        "end":"2022-11-07T16:30:00+01",
        "url":"",
        "nomModule":"",
        "matiere":null,
        "theme":"",
        "salles":[
            {
                "nomSalle":"N102"
            },
            {
                "nomSalle":"N104A CPI A2"
            },
            {
                "nomSalle":"N104B CPI A2"
            },
            {
                "nomSalle":"N214B FISA"
            }
        ],
        "intervenants":null,
        "participantsPersonne":null,
        "participants":[
            {
                "libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète",
                "codeGroupe":"155923",
                "codeSession":"2182217"
            }
        ]
    },
    {
        "code":"4019719","title":"A planifier","allDay":false,"nightly":false,"start":"2022-11-08T09:00:00+01","end":"2022-11-08T12:30:00+01","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"},{"nomSalle":"N104A CPI A2"},{"nomSalle":"N104B CPI A2"}],"intervenants":null,"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète","codeGroupe":"155923","codeSession":"2182217"}]},{"code":"4019720","title":"A planifier","allDay":false,"nightly":false,"start":"2022-11-08T13:30:00+01","end":"2022-11-08T16:30:00+01","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"},{"nomSalle":"N104A CPI A2"},{"nomSalle":"N104B CPI A2"}],"intervenants":null,"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète","codeGroupe":"155923","codeSession":"2182217"}]},{"code":"4019721","title":"A planifier","allDay":false,"nightly":false,"start":"2022-11-09T09:00:00+01","end":"2022-11-09T12:30:00+01","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"},{"nomSalle":"N104A CPI A2"},{"nomSalle":"N104B CPI A2"}],"intervenants":null,"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète","codeGroupe":"155923","codeSession":"2182217"}]},{"code":"4058695","title":"Travail de groupe","allDay":false,"nightly":false,"start":"2022-11-09T13:30:00+01","end":"2022-11-09T17:30:00+01","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"},{"nomSalle":"N104A CPI A2"},{"nomSalle":"N104B CPI A2"}],"intervenants":null,"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Autonomie - Anglais","codeGroupe":"181277","codeSession":"2182217"}]},{"code":"4054982","title":"Anglais","allDay":false,"nightly":false,"start":"2022-11-09T15:00:00+01","end":"2022-11-09T16:30:00+01","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"S224 Poly"}],"intervenants":[{"sousTitre":null,"profils":null,"groupesPedagogiques":null,"urlFiche":"https://ent.cesi.fr/servlet/urlfiche?OBJET=PERSONNE&CODE=2194170&LANGUE=0","urlPhoto":"https://ent.cesi.fr/images/fo/avatar-homme.jpg","nom":"SMITH","prenom":"Ian","code":"2194170","adresseMail":"","urlAgenda":"","sessions":[],"inconnu":false}],"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Anglais - Groupe 6","codeGroupe":"180851","codeSession":"2182217"}]}]
  

l_cour_1 = {
}
l_cour_2 = {
    "title": "lundi2",
    "start": "start",
    "end": "end"
}
l_cour_3 = {
    "title": "lundi3",
    "start": "start",
    "end": "end"
}
l_cour_4 = {
    "title": "lundi4",
    "start": "start",
    "end": "end"
}
div_Lundi = [l_cour_1, l_cour_2, l_cour_3, l_cour_4]

Ma_cour_1 = {
    "title": "mardi1",
    "start": "start",
    "end": "end"
}
Ma_cour_2 = {
    "title": "mardi2",
    "start": "start",
    "end": "end"
}
Ma_cour_3 = {
    "title": "Mardi3",
    "start": "start",
    "end": "end"
}
Ma_cour_4 = {
    "title": "Mardi4",
    "start": "start",
    "end": "end"
}
div_Mardi = [Ma_cour_1, Ma_cour_2, Ma_cour_3, Ma_cour_4]

Me_cour_1 = {
    "title": "Mercredi1",
    "start": "start",
    "end": "end"
}
Me_cour_2 = {
    "title": "Mercredi2",
    "start": "start",
    "end": "end"
}
Me_cour_3 = {
    "title": "Mercredi3",
    "start": "start",
    "end": "end"
}
Me_cour_4 = {
    "title": "Mercredi4",
    "start": "start",
    "end": "end"
}
div_Mercredi = [Me_cour_1, Me_cour_2, Me_cour_3, Me_cour_4]

j_cour_1 = {
    "title": "Jeudi1",
    "start": "start",
    "end": "end"
}
j_cour_2 = {
    "title": "Jeudi2",
    "start": "start",
    "end": "end"
}
j_cour_3 = {
    "title": "Jeudi3",
    "start": "start",
    "end": "end"
}
j_cour_4 = {
    "title": "Jeudi4",
    "start": "start",
    "end": "end"
}
div_Jeudi = [j_cour_1, j_cour_2, j_cour_3, j_cour_4]

v_cour_1 = {
    "title": "Vendredi1",
    "start": "start",
    "end": "end"
}
v_cour_2 = {
    "title": "Vendredi2",
    "start": "start",
    "end": "end"
}
v_cour_3 = {
    "title": "Vendredi3",
    "start": "start",
    "end": "end"
}
v_cour_4 = {
    "title": "Vendredi4",
    "start": "start",
    "end": "end"
}
div_Vendredi = [v_cour_1, v_cour_2, v_cour_3, v_cour_4]


div_day = [div_Lundi, div_Mardi, div_Mercredi, div_Jeudi, div_Vendredi]

Lundi = ""

Mardi = ""
Mercredi = ""
Jeudi = ""
Vendredi = ""
day = [Lundi, Mardi, Mercredi, Jeudi, Vendredi]


d = 0
h = 0

for d in range(len(div_day)):
    div = ""
    for h in range(len(response_)):
        title = str(response_[h]["title"]) + '\n'
        hour = str(response_[h]["start"].partition("T")[2].removesuffix(":00+02")) + " - " + str(response_[h]["end"].partition("T")[2].removesuffix(":00+02")) + '\n\n'
        div = div + title + hour
    day[d] = div

day_name = [
            "  Lundi ",
            "  Mardi ",
            "Mercredi",
            "  Jeudi ",
            "Vendredi"]

d = -1

post_ = True

if post_:
    for d in range(d,len(day)):  

        if d == -1:
            data["embeds"] = [
                {
                    "type": "rich",
                    "title": "Emploi du temps de la semaine:",
                    "color": 0xFBE214
                    }
                ]
        elif d >= 0:
            data["embeds"] = [
                {
                    "type": "rich",
                    "description": "",
                    "title": day_name[d],
                    "color": 0xDDDDDD,
                    "fields": [
                        {
                            "name": day[d],
                            "value": "\u200B"
                        }
                    ],
                }
            ]
        elif d == 4:
            print("yousk2")
            data["footer"] = {
                "text": "source: https://ent.cesi.fr/api/seance/",
                "icon_url": "https://yt3.ggpht.com/ytc/AMLnZu-r9SK3rtCm-hF3UlW1nolyr8mIBJS10FBnIKFDHw=s900-c-k-c0x00ffffff-no-rj"
                }


        result = requests.post(url, json=data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
            print(d)
            
        d+1
