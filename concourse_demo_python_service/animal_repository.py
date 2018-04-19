def fetch_by_letter(letter):
    animals = {
        'd': 'Dog',
        'c': 'Cat',
        's': 'Snake'
    }

    if letter.lower() not in animals:
        raise AnimalNotFound()

    return animals[letter.lower()]

class AnimalNotFound(Exception):
    pass