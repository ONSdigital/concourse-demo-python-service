def fetch_by_letter(letter):
    colours = {
        'r': 'Red',
        'g': 'Green',
        'b': 'Blue'
    }

    try:
        return colours[letter.lower()]
    except KeyError:
        raise ColourNotFound()


class ColourNotFound(Exception):
    pass