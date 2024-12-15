def resolve_anaphora(pronoun, context):
    import requests
    from config.settings import JDM_API_URL

    for word in context:
        response = requests.get(f"{JDM_API_URL}/related/{word}/{pronoun}")
        if response.status_code == 200 and response.json().get("found"):
            return word
    return None
