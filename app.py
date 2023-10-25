from flask import Flask, jsonify, request, render_template

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

@app.route('/form')
def mostrar_formulario():
    return render_template('formulario.html')

# Endpoint para procesar la donación y agregarla al archivo donaciones.py
@app.route('/donar', methods=['POST'])
def donar():
    criptomoneda = request.form.get('criptomoneda')
    cantidad = request.form.get('cantidad')

    # Agregar la donación al archivo donaciones.py
    from donaciones import donaciones  # Importar la lista de donaciones desde donaciones.py
    donaciones.append({"criptomoneda": criptomoneda, "cantidad": cantidad})

    return "Donación exitosa"


if __name__ == '__main__':
    app.run(debug=True, port=4000)
