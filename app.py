<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
@app.route('/')
=======

from flask import Flask
app = Flask(__name__)
@app.route('/')

>>>>>>> 79ae6d840f0b166fe2cea3900fe37d0a8a70da68
def hello_world():
    return 'Hello world'