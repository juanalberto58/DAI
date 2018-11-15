from flask import Flask, render_template, session, request, redirect, flash
from pickleshare import *
import os

app = Flask(__name__)

db = PickleShareDB('~/testpickleshare')
db.clear()

db['Juan Alberto'] = {'Apellido':'Rivera','DNI':'76665328'}
db['Juan'] = {'Apellido':'Martin','DNI':'76842349'}

usuarios = db.keys()

@app.route("/")
def home():
    if 'username' in session:
        username = session['username']
        return render_template('main.html', username = username)
    else:
        return render_template('main.html')

@app.route('/menu1')
def menu1():
    if 'username' in session:
        username = session['username']
        return render_template('menu1.html', username = username)
    else:
        return render_template('menu1.html')

@app.route('/menu2')
def menu2():
    if 'username' in session:
        username = session['username']
        return render_template('menu2.html', username = username)
    else:
        return render_template('menu2.html')

@app.route('/menu3')
def menu3():
        if 'username' in session:
            username = session['username']
            return render_template('menu3.html', username = username)
        else:
            return render_template('menu3.html')

@app.route('/login', methods=['POST'])
def login():
    name=request.form.get('username')
    if name in usuarios:
        session['username']=name
    return redirect('/')

@app.route('/usuario')
def usuario():
    if 'username' in session:
        username = session['username']
        lastname = db[username]['Apellido']
        dni = db[username]['DNI']
        return render_template('usuario.html', username = username, lastname=lastname, dni=dni)
    else:
        return redirect('/')

@app.route('/registro')
def register():
    return render_template('registro.html')

@app.route('/cambiodatos')
def cambiodatos():
        if 'username' in session:
            username = session['username']
            return render_template('cambiodatos.html', username = username)
        else:
            return redirect('/')

@app.route('/cambio', methods=['POST'])
def cambio():
        username=session['username']
        name=request.form.get('name')
        apellido=request.form.get('lastname')
        dni=request.form.get('dni')

        session['username'] = name

        db[name]=db[username]
        db[name]['Apellido']=apellido
        db[name]['DNI']=dni

        return render_template('cambiodatos.html', username = name, apellido=apellido, dni=dni)

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
