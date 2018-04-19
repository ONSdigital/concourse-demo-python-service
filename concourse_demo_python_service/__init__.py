from flask import Flask, request

from concourse_demo_python_service import animal_repository, colour_repository
from concourse_demo_python_service.animal_repository import AnimalNotFound
from concourse_demo_python_service.colour_repository import ColourNotFound

app = Flask(__name__)


@app.route('/coloured_animal')
def coloured_animal():
    try:
        animal_letter = request.args['animal']
        colour_letter = request.args['colour']

        animal = animal_repository.fetch_by_letter(animal_letter)
        colour = colour_repository.fetch_by_letter(colour_letter)

        return f'{colour} {animal}'
    except KeyError:
        return 'Missing argument', 400
    except ColourNotFound:
        return 'Colour not found', 404
    except AnimalNotFound:
        return 'Animal not found', 404
