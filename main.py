from chaine_caracteres import *
from les_types import *
from structures import *
from boucles import *

# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    base = ""
    while base != "/X":
        fonction = ""
        base = input("Quelle partie commencer ? \n"
                     "Taper 1 pour des tests sur les types ;\n"
                     "Taper 2 pour des tests sur les chaines de caractères ;\n"
                     "Taper 3 pour des tests sur les conditions (if) ; \n"
                     "Taper 4 pour des tests sur les boucles ; \n"
                     "taper \"/X\" pour quitter.").upper()

        if base == "1":
            while fonction != "/X":
                fonction = input("Quelle fonction exécuter ?\n"
                                 "taper 1 pour voir la liste des différentes options de cast avec l'opérateur Modulo (%) ;\n"
                                 "taper 2 pour voir les méthodes pour concaténer 2 valeurs de types différents ;\n"
                                 "taper 3 pour connaitre le type d'une valeur ; \n"
                                 "taper \"/X\" pour revenir à l'action précédente.").upper()
                if fonction == "1":
                    list_de_cast_operator()
                elif fonction == "2":
                    concat_int_and_string(input("Entrez une valeur de type integer (int)"), input("Entrez une valeur de type chaine de caractères (str)"))
                    supprimer_espace_dans_print()
                elif fonction == "3":
                    les_types(input("Entrez une valeur pour connaitre son type"))
                elif fonction == "/X":
                    print("A bientôt.")
                else:
                    print("La valeur entrée ne correspond à aucune fonction.")

        elif base == "2":
            while fonction != "/X":
                fonction = input("Quelle fonction exécuter ?\n"
                                 "taper 1 pour connaitre les options de cast en string avec l'opérateur \"modulo\" sur les différents types ;\n"
                                 "taper 2 pour concaténer un integer (int) avec une chaine de caractères (str) ;\n"
                                 "taper 3 pour un exemple avec et sans espace automatique dans un print ; \n"
                                 "taper 4 pour un exemple de message avec les consonnes cachées ; \n"
                                 "taper \"/X\" pour revenir à l'action précédente.").upper()
                if fonction == "1":
                    list_de_cast_operator()
                elif fonction == "2":
                    concat_int_and_string(input("Entrez un entier : "), input("Entrez une chaine de caractères : "))
                elif fonction == "3":
                    supprimer_espace_dans_print()
                elif fonction == "4":
                    cacher_les_lettres(input("taper A, E, I, O, U ou Y pour cacher les VOYELLES, Le reste pour cacher les consonnes : "))
                else:
                    print("La valeur entrée ne correspond à aucune fonction.")

        elif base == "3":
            while fonction != "/X":
                fonction = input("Quelle fonction exécuter ?\n"
                                 "taper 1 pour voir un if à l'action ;\n"
                                 "taper \"/X\" pour revenir à l'action précédente.").upper()
                if fonction == "1":
                    test_if()

        elif base == "4":
            fonction = input("Quelle fonction exécuter ?\n"
                             "taper 1 pour travailler avec la boucle WHILE ;\n"
                             "taper 2 pour travailler avec la boucle FOR ;\n"
                             "taper \"/X\" pour revenir à l'action précédente.").upper()
            if fonction == "1":
                basic_while(input("Entrez une valeur pour obtenir sa table de multiplication :"))
            elif fonction == "2":
                basic_for(input("Entrez le message à extraire lettre par lettre : "))

        elif base == "/X":
            print("Au revoir.")
            
        else:
            print("La valeur entrée ne correspond à aucune fonction.")
