#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request # HTTP request sent by client and received by server
app = Flask(__name__)

@app.route('/coucou/')
def dire_coucou():
    return 'Coucou !'

# The page path can be accessed through the path attribute

@app.route('/')
def racine():
    return "Le chemin de 'racine' est : " + request.path

@app.route('/la/')
def ici():
    return "Le chemin de 'ici' est : " + request.path

"""
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        # if the user arrives to the page, the method will be GET
        # afficher le formulaire
        return "afficher le formulaire"
    else:
        # If the user just validated the form, the method will be POST
        # traiter les données reçues
        # afficher : "Merci de m'avoir laissé un message !"
        return "Merci de m'avoir laissé un message !"

"""

"""
# récupérer le message envoyé par le visiteur et le lui afficher :
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fichier = request.files['mon_fichier']
        nom_fichier = fichier.filename
        # sauvegarder un fichier dans le dossier './uploads'
        if nom_fichier[-5:] != '.html':
            nom_fichier = secure_filename(nom_fichier)
            fichier.save('./uploads/' + nom_fichier)
        return "Vous avez envoyé : {msg}".format(msg=request.form.get('msg', "Vous n avez rien envoyé"))
    return '<form action="" method="post"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'
"""

@app.route('/contact/') # on n'autorise pas la méthode POST
def contact():
    if request.args.get('msg') is not None:
        return "Vous avez envoyé : {msg}".format(msg=request.args['msg'])
    return '<form action="" method="get"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'

"""
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Vous avez envoyé un message..."
    return '<form action="" method="post"><input type="text" name="msg" />input type="submit" value="Envoyer" /></form>'
"""

"""
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    request.form.get('msg', 'valeur par defaut')
    if request.method == 'POST':
        return "Vous avez envoyé : {msg}".format(msg=request.form['msg'])
    return '<form action="" method="post"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'
"""

@app.route('/debug/')
def debug():
    raise Exception('xyz')
    
"""
# different views for different methods

@app.route('/contact/', methods=['GET'])
def contact_formulaire():
    #afficher le formulaire
    return "if"


@app.route('/contact/', methods=['POST'])
def contact_traiter_donnees():
    # traiter les données reçues
    # afficher : "Merci de m'avoir laissé un message !"
    return "else"
"""
# 1 vue, multiple routes

@app.route('/f_python')
@app.route('/forum/python')
@app.route('/truc')
def forum_python():
    return 'contenu forum python'

"""
# Multiple personnalized routes/ vue

@app.route('/discussion/page/<num_page>/')
def mon_chat(num_page):
    num_page = int(num_page)
    premier_msg = 1 + 50 * (num_page - 1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)
"""

"""
# access 50 1st messages through '/discussion' address

@app.route('/discussion/')
# convert string to num
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
    premier_msg = 1 + 50 * (num_page - 1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)
"""

# routes personnalisées
@app.route('/discussion/page/<int:num_page>')
def discussion(num_page):
    return 'Affichage de la page n°{num} de la discussion.'.format(num=num_page)
    
"""    
    url_for('discussion', num_page=3, truc='machin') # generate '/discussion/page/3?truc=machin'
    url_for('discussion', num_page=12, truc='machin', age=20) # generate '/discussion/page/12?truc=machin&age=20'
"""   

@app.route('/afficher')
@app.route('/afficher/mon_nom_est_<nom>_et_mon_prenom_<prenom>')
def afficher(nom=None, prenom=None):
    if nom is None or prenom is None:
        return "Entrez votre nom et votre prénom comme il le faut dans l'url"
    return "Vous vous appelez {} {} !".format(prenom, nom)

if __name__ == '__main__':
    app.run(debug=True)