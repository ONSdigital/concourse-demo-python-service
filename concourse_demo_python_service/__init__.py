from flask import Flask

from concourse_demo_python_service import animal_repository

app = Flask(__name__)


@app.route('/coloured_animal')
def coloured_animal():
    return 'Red ' + animal_repository.fetch_by_letter('c')