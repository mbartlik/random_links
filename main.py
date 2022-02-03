import os
from os import path

from flask import Flask
from flask import render_template
from flask import url_for

import requests
import json


app = Flask(__name__)

app.secret_key = 'apdsifjgr'

global latest_link
latest_link = ''

@app.route("/")
def index():
    return render_template('index.html', link = 'ksahbdgruefsaoidnfsvbefwiasnbudviad.com')

@app.route("/fun-link")
def fun_link():
    global latest_link

    while True:
        query = requests.get('https://random-links-api.uk.r.appspot.com/fun-link').json()
        link = query['link']
        description = query['description']

        if link != latest_link:
            break

    latest_link = link

    return render_template('index.html', link=link, description=description)

@app.route("/game-link")
def game_link():
    global latest_link

    while True:
        query = requests.get('https://random-links-api.uk.r.appspot.com/game-link').json()
        link = query['link']
        description = query['description']

        if link != latest_link:
            break

    latest_link = link

    return render_template('index.html', link=link, description=description)

@app.route("/news-link")
def news_link():
    global latest_link

    while True:
        query = requests.get('https://random-links-api.uk.r.appspot.com/news-link').json()
        link = query['link']
        description = query['description']

        if link != latest_link:
            break

    latest_link = link

    return render_template('index.html', link=link, description=description)