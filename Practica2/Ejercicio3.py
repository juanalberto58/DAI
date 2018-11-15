from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Zerjillo, hola Pepe"

@app.route('/user/pepe')
def Pepe():
    return "Bienvenido Pepe!!"

@app.route('/user/zerjillo')
def Zerjillo():
    return "Bienvenido Zerjillo!!!"

@app.route('/user/<user>')
def redirige(user):
        return "Bienvenido "+user+"!!!"

@app.errorhandler(404)
def access_error(error):
    return "Página web no encontrada", 404

app.run(host='0.0.0.0', debug=True)
