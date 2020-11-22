def test_if():
    majorite = 18
    age = ""
    while not age.isdigit():
        age = input("Entrez votre age :")
        if not age.isdigit():
            print("Vous n'avez pas entrez de valeur valide.")
        elif int(age) > majorite:
            print("Vous êtes majeur :) A la votre !")
        else:
            print("Vous êtes mineur ! ")
