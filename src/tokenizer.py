def tokenize_and_detect_composite_terms(text):
    print("Texte reçu pour tokenisation :", text)
    words = text.split()
    print("Mots identifiés :", words)
    return words  # Vérifiez si les mots sont bien renvoyés


def is_composite_term(term):
    import requests
    response = requests.get(f"https://jdm-api.demo.lirmm.fr/term/{term}")
    print(f"Requête envoyée pour le terme : {term}, statut :", response.status_code)
    if response.status_code == 200:
        print(f"Réponse de l'API pour {term} :", response.json())
    return response.status_code == 200 and response.json().get("found", False)
