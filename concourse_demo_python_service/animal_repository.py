def fetch_by_letter(letter):
    animals = {
        'd': 'Dog',
        'c': 'Cat',
        's': 'Snake'
    }

    try:
        return animals[letter.lower()]
    except KeyError:
        raise AnimalNotFound()

class AnimalNotFound(Exception):
    pass
