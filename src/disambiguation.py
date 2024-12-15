import requests
from config.settings import JDM_API_URL

def disambiguate_word(word, context):
    response = requests.get(f"{JDM_API_URL}/term/{word}/out")
    candidates = response.json().get("relations", [])
    best_candidate = max(candidates, key=lambda x: x["weight"], default=None)
    return best_candidate["dest"] if best_candidate else None
