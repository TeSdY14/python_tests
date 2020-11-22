def bissextil_or_not(annee):
    annee_bissextile_ok = annee + " est bissextile"
    annee_bissextile_ko = annee + " n'est pas bissextile"
    print("annee est de type : \n", type(annee), "\nIl faut donc caster cette valeur en String")
    annee_int = int(annee)
    print("annee_int est maintenant de type : \n", type(annee_int), "\nOn est bon!")
    # Une annee est bissextile :
    # SI ELLE EST MULTIPLE DE 400 ALORS OUI !
    # SI ELLE EST MULTIPLE DE 4 MAIS PAS MULTIPLE DE 100 (sauf si multiple de 400)
    # les deux seuls cas correspondant à une année bissextile sont « si l'année est un multiple de 400 »ou « si l'année est un multiple de 4 mais pas de 100 ».
    if annee_int % 400 == 0 or (annee_int % 4 == 0 and annee_int % 100 != 0):
        print(annee_bissextile_ok)
    else:
        print(annee_bissextile_ko)


annee = ""
value = input("Entrez une année pour savoir si elle est bissextile : ")
while value.isdigit():
    bissextil_or_not(value)
    value = input("Entrez une année pour savoir si elle est bissextile : ")
print("Au revoir.")
