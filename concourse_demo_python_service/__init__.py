from flask import Flask

app = Flask(__name__)


@app.route('/coloured_animal')
def coloured_animal():
    return "Red Cat"
