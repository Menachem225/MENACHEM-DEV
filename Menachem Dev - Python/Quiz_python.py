import random

regions = {
    "Abidjan": "Abidjan",
    "Agneby-Tiassa": "Agboville",
    "Belier": "Yamoussoukro",
    "Bleketre": "Divo",
    "Bouafle": "Bouafle",
    "Boukani": "Bouna",
    "Cavally": "Guiglo",
    "Dix-Huit Montagnes": "Man",
    "Fromager": "Gagnoa",
    "Gbeke": "Bouaké",
    "Gbêkê": "Bouaké",
    "Grand Bassam": "Grand Bassam",
    "Guemon": "Bangolo",
    "Haut-Sassandra": "Daloa",
    "Indenie-Djuablin": "Abengourou",
    "Kabadougou": "Ferké",
    "Loh-Djiboua": "Zoukougbeu",
    "Marahoué": "Bouaflé",
    "Moronou": "Bongouanou",
    "Nawa": "Soubré",
    "N'Zi": "Dimbokro",
    "Poro": "Korhogo",
    "San-Pedro": "San-Pedro",
    "Sassandra": "Sassandra",
    "Sud-Bandama": "Divo",
    "Sud-Comoé": "Aboisso",
    "Tchologo": "Ferkessédougou",
    "Tonkpi": "Man",
    "Valle du Bandama": "Bouaké",
    "Worodougou": "Séguéla",
    "Yamoussoukro": "Yamoussoukro"
}

def debut():
    questions_quiz = random.sample(list(regions.items()), 10)
    score = 0

    print("Bienvenue au Quiz des Régions de Côte d'Ivoire !")
    print("Répondez aux questions suivantes sur les régions ivoiriennes et leurs chefs-lieux.\n")

    for region, Cl_correct in questions_quiz:
        print(f"Quel est le chef-lieu de la région {region} ?")
        reponse_user = input("Votre réponse : ").strip()
        if reponse_user.lower() == Cl_correct.lower():
            print("Correct ! 🎉")
            score += 1
        else:
            print(f"Incorrect ! Le chef-lieu de la région {region} est {Cl_correct}.")

    print(f"\nJeu terminé ! Votre score : {score}/10")
    rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
    return rejouer == 'oui'

def principale():
    while True:
        if not debut():
            print("Merci ")
            break

if __name__ == "__main__":
    principale()
