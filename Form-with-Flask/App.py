from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à la base de données MongoDB
uri = "mongodb+srv://giuseppe:sesame@cluster0.0hsxtkf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client['Cluster0']
collection = db['Formulaire2']

@app.route('/', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        commentaire = request.form['commentaire']
        
        # Insérer les données dans la base de données MongoDB
        collection.insert_one({'nom': nom, 'prenom': prenom, 'email': email, 'commentaire': commentaire})
        
        return 'Données enregistrées avec succès !'
    
    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run()
