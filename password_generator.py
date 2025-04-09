import secrets
import string


def demander_criteres():
    """demande a l'utilisateur les criteres du mot de passe a generer et vérifie les conditions:
    entre 8 et 50 ET si c'est un nombre, pas autre chose
    """

    while True:
        longueur = input("Quelle longueur de mot de passe veux-tu ? (entre 8 et 50) : \n")
        try:
            longueur = int(longueur)
            if 8 <= longueur <= 50:
                return longueur
            print("Tu dois entrer un nombre entre 8 et 50\n")
        except ValueError:
            print("Tu dois entrer un nombre valide !\n")

def demander_oui_non(question):
    """fonction qui demande a l'utilisateur de choisir si il veut des majuscules,
    minuscules, chiffres et caracteres spéciaux dans son mot de passe"""

    while True:
        reponse = input(question + " ").strip().lower()
        if reponse == "oui":
            return True
        if reponse == "non":
            return False
        print("Merci de répondre par 'oui' ou 'non'.")

def construire_liste_caracteres(majuscule, minuscule, chiffre, speciaux):
    """fonction qui permer de contruire la liste de caracteres qui sera utilisée pour
    construire le mot de passe    en fonction des choix de l'utilisateur
    """

    liste = []
    majuscules = string.ascii_uppercase
    minuscules = string.ascii_lowercase
    chiffres = string.digits
    special = string.punctuation

    if majuscule:
        liste.extend(majuscules)
    if minuscule:
        liste.extend(minuscules)
    if chiffre:
        liste.extend(chiffres)
    if speciaux:
        liste.extend(special)
    return liste


def generation_mot_de_passe(liste_caracteres, longueur):
    mot_de_passe = ""
    for i in range(longueur):
        caractere_aleatoire = secrets.choice(liste_caracteres)
        mot_de_passe += caractere_aleatoire
    print(f"Voici votre mot de passe de {longueur} caractères: ")
    print(mot_de_passe)


def jouer():
    """fonction principale de jeu"""


    print("Bienvenue dans le générateur de mots de passe sécurisés ! 🔒\n")
    longueur = demander_criteres()
    while True:
        inclure_majuscules = demander_oui_non("Inclure des majuscules ? (oui/non) :")
        inclure_minuscules = demander_oui_non("Inclure des minuscules ? (oui/non) :")
        inclure_chiffres = demander_oui_non("Inclure des chiffres ? (oui/non) :")
        inclure_caracteres_speciaux = demander_oui_non("Inclure des caracteres_speciaux ? (oui/non) :")

        liste_caracteres = construire_liste_caracteres(
        inclure_majuscules,
        inclure_minuscules,
        inclure_chiffres,
        inclure_caracteres_speciaux)
        if not liste_caracteres:
            print("Tu dois sélectionner au moins un type de caractère pour générer un mot de passe.")
        else:
            break
    generation_mot_de_passe(liste_caracteres, longueur)
jouer()
