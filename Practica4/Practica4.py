from flask import Flask, request, render_template, session, redirect, url_for
from pickleshare import *
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient('localhost',27017)

mongo = client['Restaurants']
collectionRes = mongo['RestaurantsCollection']

db = PickleShareDB('~/testpickleshare')
db.clear()

db['Juan Alberto'] = {'Apellido':'Rivera','DNI':'76665328'}
db['Juan'] = {'Apellido':'Martin','DNI':'12345678'}

usuarios = db.keys()

@app.route('/login', methods=['POST'])
def login():
    name=request.form.get('username')
    if name in usuarios:
        session['username']=name
    return redirect('/')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registrado', methods=['POST'])
def registrado():
    if request.form.get('submit')=="registrar":
        print ("akjdfñhdsfñiuasgfuhasdf")
        newuser=request.form.get('nusername')
        newlastname=request.form.get('lastname')
        newdni =request.form.get('dni')
        db[newuser]={'Apellido':newlastname,'DNI':newdni}
        usuarios=db.keys()
        print(usuarios)
        return render_template('registro.html', rendered=True)
    else:
        return render_template('registro.html')


@app.route('/perfil')
def usuario():
    if 'username' in session:
        username = session['username']
        lastname = db[username]['Apellido']
        dni = db[username]['DNI']
        return render_template('perfil.html', username = username, lastname=lastname, dni=dni)
    else:
        return redirect('/')

@app.route('/buscar', methods=['POST'])
def buscar():
    if 'username' in session:
        username = session['username']
        nombre=request.form.get('namer')
        item = collectionRes.find({'name': nombre})
        return render_template('buscar.html', username = username, nameres=item)

@app.route('/insertado', methods=['POST'])
def insertado():
    if 'username' in session:
        username = session['username']
        if request.form.get('submit')=="insertar":
            namei=request.form.get('name')
            lati=request.form.get('lat')
            longi=request.form.get('long')
            data={'location': {'coordinates': [longi, lati], 'type': 'Point'}, 'name': namei}
            collectionRes.insert(data)
            return render_template('insertar.html', username = username, rendered=True)
        else:
            return render_template('insertar.html', username = username)

@app.route('/insertar')
def insertar():
    if 'username' in session:
        username = session['username']
        return render_template('insertar.html', username = username)

@app.route('/modificar')
def modificar():
    if 'username' in session:
        username = session['username']
        return render_template('modificar.html', username = username)

@app.route('/modificado', methods=['POST'])
def modificado():
    if 'username' in session:
        username = session['username']
        if request.form.get('submit')=="modificar":
            oldname=request.form.get('oldnameres')
            newname=request.form.get('newnameres')
            newlongi=request.form.get('newlong')
            newlati=request.form.get('newlati')
            collectionRes.update( {'name':oldname} , {"$set": {'location': {'coordinates': [newlongi, newlati], 'type': 'Point'}, 'name': newname}} )
            return render_template('modificar.html', username = username, rendered=True)
        else:
            return render_template('modificar.html', username = username)


@app.route('/mostrar')
def mostrar():
    if 'username' in session:
        username = session['username']
        listitem=collectionRes.find()
        return render_template('mostrar.html', username = username, listitem=listitem)

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username = username)
    else:
        return render_template('index.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def access_error(error):
    return "Página web no encontrada", 404


if __name__ == "__main__":
        app.secret_key = os.urandom(24)
        app.run(host='0.0.0.0', debug=True)
