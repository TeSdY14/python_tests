def basic_while(repetition):
    print("Table de multiplication de " + repetition)
    limit_basse = int(input("Multiplicateur mini de la multiplication : "))
    limit_haute = int(input("Multiplicateur maxi de la multiplication : "))

    while limit_basse <= limit_haute:
        print(repetition, "x", limit_basse, "=", int(repetition) * limit_basse)
        limit_basse += 1


def basic_for(message):
    i = 0
    print("Analyse d'une chaine de caractères : " + "(" + message + ")")
    for lettre in message:
        i += 1
        print(i, ":", lettre)

    print("Il y a ", i, " caractères dans : «", message, "»", sep='')
