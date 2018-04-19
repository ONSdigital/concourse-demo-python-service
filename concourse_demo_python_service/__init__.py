from flask import Flask, request

from concourse_demo_python_service import animal_repository, colour_repository
from concourse_demo_python_service.animal_repository import AnimalNotFound
from concourse_demo_python_service.colour_repository import ColourNotFound

app = Flask(__name__)


@app.route('/coloured_animal')
def coloured_animal():
    try:
        colour = colour_repository.fetch_by_letter(request.args.get('colour'))
        animal = animal_repository.fetch_by_letter(request.args.get('animal'))

        return f'{colour} {animal}'

    except ColourNotFound:
        return 'Colour not found', 404
    except AnimalNotFound:
        return 'Animal not found', 404
