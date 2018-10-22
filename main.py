#!/usr/bin/python3

from gpiozero import LED
from flask import Flask

app = Flask(__name__)

@app.route("/")
def ready():

    return "Server beschikbaar\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0')