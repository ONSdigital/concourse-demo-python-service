from flask import Flask, request

from concourse_demo_python_service import animal_repository, colour_repository

app = Flask(__name__)


@app.route('/coloured_animal')
def coloured_animal():
    colour = colour_repository.fetch_by_letter(request.args.get('colour'))
    animal = animal_repository.fetch_by_letter(request.args.get('animal'))

    return f'{colour} {animal}'
