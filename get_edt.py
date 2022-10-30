import requests

if __name__ is z:
    null = 0
    false = False

    response_ = [{"code":"4090524","title":"Travail de groupe","allDay":false,"nightly":false,"start":"2022-10-28T09:00:00+02","end":"2022-10-28T12:30:00+02","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"},{"nomSalle":"N104A CPI A2"},{"nomSalle":"N104B CPI A2"}],"intervenants":[{"sousTitre":null,"profils":null,"groupesPedagogiques":null,"urlFiche":"https://ent.cesi.fr/servlet/urlfiche?OBJET=PERSONNE&CODE=1228634&LANGUE=0","urlPhoto":"https://ent.cesi.fr/images/fo/avatar-homme.jpg","nom":"AMAMOU","prenom":"Mohamed","code":"1228634","adresseMail":"","urlAgenda":"","sessions":[],"inconnu":false}],"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Groupe session complète","codeGroupe":"155923","codeSession":"2182217"}]},{"code":"4107205","title":"Prosit aller","allDay":false,"nightly":false,"start":"2022-10-28T13:30:00+02","end":"2022-10-28T15:00:00+02","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"}],"intervenants":[{"sousTitre":null,"profils":null,"groupesPedagogiques":null,"urlFiche":"https://ent.cesi.fr/servlet/urlfiche?OBJET=PERSONNE&CODE=2430574&LANGUE=0","urlPhoto":"https://ent.cesi.fr/images/fo/avatar-homme.jpg","nom":"MAHIEU","prenom":"Romain","code":"2430574","adresseMail":"","urlAgenda":"","sessions":[],"inconnu":false}],"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Bloc Electronique - Groupe Romain - N 102","codeGroupe":"182358","codeSession":"2182217"}]},{"code":"4107209","title":"Travail de groupe","allDay":false,"nightly":false,"start":"2022-10-28T15:00:00+02","end":"2022-10-28T16:00:00+02","url":"","nomModule":"","matiere":null,"theme":"","salles":[{"nomSalle":"N102"}],"intervenants":null,"participantsPersonne":null,"participants":[{"libelleGroupe":"CPI A1 22-23 Rouen - Bloc Electronique - Groupe Romain - N 102","codeGroupe":"182358","codeSession":"2182217"}]}]




    for x in range(len(response_)):
        print('\n')
        print(len(response_[x]))
        keys = response_[x].keys()
        values = response_[x].values()

        for k, v in response_[x].items():
            globals()[k] = v

            print(x,':',k,'-->', v)
        print('\n')

