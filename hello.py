#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route('/')


def accueil():
    """
    mots = ["bonjour", "à", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)
    """
    return render_template('accueil.html')

from datetime import date

@app.route('/date')
def date():
    d = date.today().isoformat()
    return render_template('accueil')


if __name__ == '__main__':
    app.run(debug=True)