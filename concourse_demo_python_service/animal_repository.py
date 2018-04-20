import os
import requests

def fetch_by_letter(letter):
    response = requests.get(os.getenv("ANIMAL_SERVICE") + "/animal/" + letter.lower())

    if response.status_code == 404:
        raise AnimalNotFound()

    return response.text

class AnimalNotFound(Exception):
    pass
