from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

from cryptos import cryptos
from donaciones import donaciones
from politicasyterminosdeuso import politicasyterminosdeuso, reglas
from politicasdeprivacidad import politicasdeprivacidad, informacionquerecopilamos, usodelainformacion, compartirinformacion, seguridaddedatos, cookiesytecnologiassimilares, cambiosenlapoliticadeprivacidad, contacto

@app.get("/")
def home():
    return render_template ("home.html")

@app.route('/cryptos')
def getcryptos():
    return jsonify({'cryptos': cryptos})

@app.route('/politicas-y-terminos-de-uso')
def getpoliticasyterminosdeuso():
    return jsonify({'Politicas y Terminos de Uso': politicasyterminosdeuso, 'Reglas':reglas})
    

@app.route('/politicas-de-privacidad')
def getpoliticasdeprivacidad():
    return jsonify({ 'Politicas de Privacidad': politicasdeprivacidad,'Info. que recopilamos':informacionquerecopilamos,"Uso de la info.": usodelainformacion, "Compartir info.": compartirinformacion, "Seguridad de datos": seguridaddedatos, "Cookies": cookiesytecnologiassimilares, "Cambios en la politica de privacidad": cambiosenlapoliticadeprivacidad, "Contacto": contacto })

@app.route('/donaciones', methods=['GET'])
def getdonaciones():
    return jsonify ({'donaciones': donaciones})

@app.route('/form', methods=['GET', 'POST'])
def mostrar_formulario():
    if request.method == 'POST':
       
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']

       
        donaciones.append({'nombre': nombre, 'cantidad': cantidad})

        return redirect(url_for('confirmacion'))

    return render_template('formulario.html')

@app.route('/confirmacion')
def confirmacion():
    return "Gracias por tu donación."

if __name__ == '__main__':
    app.run(debug=True, port=4000)
