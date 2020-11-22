from math import exp


def list_de_cast_operator():
    caractere = 'A'
    chaine = "une chaine"
    entier_signe1 = 156
    entier_signe2 = 221
    entier_non_signe1 = -125
    octal = 0o530
    entier_hexa1 = 0x10
    entier_hexa2 = 0x1A
    exponentiel1 = exp(1e-5)
    exponentiel2 = exp(2e-10)
    floating1 = 2.67499999999999982236431605997495353221893310546875
    shorter1 = 10.34
    shorter2 = 26.52
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LES CAST MODULO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CARACTÈRE | DESCRIPTION")
    print("    %c    | Character (Caractère)")
    print("    %s    | String conversion via str() prior to formatting. (Conversion de chaîne via str()avant le formatage).")
    print("    %i    | Signed decimal integer. (Entier décimal signé).")
    print("    %d    | Signed decimal integer. (Entier décimal signé).")
    print("    %u    | Unsigned decimal integer. (Entier décimal non signé).")
    print("    %o    | Octal integer. (Entier octal).")
    print("    %x    | Hexadecimal integer using lowercase letters. (Entier hexadécimal utilisant des lettres minuscules).")
    print("    %X    | Hexadecimal integer using uppercase letters. (Entier hexadécimal utilisant des lettres majuscules).")
    print("    %e    | Exponential notation with lowercase e. (Notation exponentielle avec minuscules e).")
    print("    %E    | Exponential notation with uppercase e. (Notation exponentielle avec minuscules e).")
    print("    %f    | Floating point real number. (Nombre réel à virgule flottante).")
    print("    %g    | The shorter of %f and %e. (Le plus court de %f et %e).")
    print("    %G    | The shorter of %f and %E. (Le plus court de %f et %E).")
    print("**Caractère : %c,\n"
          "**Chaine : %s,\n"
          "**Entier décimal signé : %i et moi aussi : %d" % (caractere, chaine, entier_signe1, entier_signe2))
    print("**Entier décimal non signé : %u,\n"
          "**Octal : %o,\n"
          "**Entier hexadécimal utilisant des lettres minuscules : %x et moi aussi : %X" % (entier_non_signe1, octal, entier_hexa1, entier_hexa2))
    print("**Exponentielle avec minuscules : %e, et moi aussi : %E,\n"
          "**Nombre réel à virgule flottante : %f" % (exponentiel1, exponentiel2, floating1))
    print("**The shorter of %%f and %%e : %g et The shorter of %%f and %%E %G" % (shorter1, shorter2))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END LES CAST MODULO END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def concat_int_and_string(entier, chaine):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CONCATENATION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("print(entier + chaine) <<<<= Donne une erreur !")
    print("print(chaine + \" - \" + str(entier)) <<<<= on cast l'entier en chaine de caractères : !")
    print("                                                                        >>>> " + chaine + " - " + str(entier) + " <<<<")
    print("print(\"%i a %s\" ans % (entier, chaine)) <<<<= On utilise l'opérateur de formatage de chaîne ou d' interpolation %type !")
    print("                                                                      >>>> " + "%s a %s ans" % (chaine, entier) + " <<<<")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END CONCATENATION END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def supprimer_espace_dans_print():
    je_suis = "Je suis un message!"
    message = "Je suis un autre message!"
    concatene = "Nous sommes concaténées!!!"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PRINT AVEC ET SANS ESPACE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Ici sans ajouter le séparateur (sep='')", "«", je_suis, message, concatene, "»")
    print("Les espaces sont ajoutés seul durant la concaténation")
    print("- ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -")
    print("Ici en ajoutant le séparateur (sep='') ", "«", je_suis, message, concatene, "»", sep='')
    print("Les espaces ne sont pas ajoutés seul car, est ajouté en paramètre : sep=''.")
    print("- ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ -")
    print("On peut séparer avec ce que l'on veut : Ici en ajoutant le séparateur (sep='*-__-*')", "«", je_suis, message, concatene, "»", sep='*-__-*')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END~PRINT AVEC ET SANS ESPACE~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def cacher_les_lettres(lettre):
    list_voyelles_lower = "aeiouy"
    list_consonnes_lower = "bcdfghjklmnpqrstvwxz"
    list_voyelles_upper = list_voyelles_lower.upper()
    list_consonnes_upper = list_consonnes_lower.upper()
    list_voyelles = list_voyelles_lower+list_voyelles_upper
    list_consonnes = list_consonnes_lower+list_consonnes_upper
    sortie = ""
    if lettre not in list_voyelles:
        filtre = list_voyelles
    else:
        filtre = list_consonnes
    message = "Bonjour je suis content"
    print("Message avec toutes les lettres :", message)
    for letter in message:
        if letter in filtre:
            letter = "*"
        print(letter)
        sortie += letter

    print(sortie)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END~END~END~END~END~END~END~END~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
