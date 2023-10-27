from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

from cryptos import cryptos
from donaciones import donaciones
from politicasyterminosdeuso import politicasyterminosdeuso, reglas
from politicasdeprivacidad import politicasdeprivacidad, informacionquerecopilamos, usodelainformacion, compartirinformacion, seguridaddedatos, cookiesytecnologiassimilares, cambiosenlapoliticadeprivacidad, contacto

@app.get("/")
def home():
    return render_template ("home.html")

@app.route('/cryptos/<crypto_code>', methods=['GET'])
def get_crypto_by_code(crypto_code):
    for crypto in cryptos:
        if crypto['codigo'] == crypto_code:
            return jsonify({'crypto': crypto})

    return jsonify({'error': 'Criptomoneda no encontrada'}), 404

@app.route('/cryptos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_cryptos():
    if request.method == 'GET':
        codigo = request.args.get('codigo')
        if codigo:
            for crypto in cryptos:
                if crypto['codigo'] == codigo:
                    return jsonify({'crypto': crypto})
            return jsonify({'error': 'Criptomoneda no encontrada'}), 404
        else:
            return jsonify({'cryptos': cryptos})
        
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Se ha agregado la criptomoneda'})
    
    elif request.method == 'PUT':
        data = request.get_json()
        return jsonify({'message': 'Se ha actualizado la criptomoneda'})
    
    elif request.method == 'DELETE':
        crypto_code = request.args.get('codigo')
        for i, crypto in enumerate(cryptos):
            if crypto['codigo'] == crypto_code:
                del cryptos[i]
                return jsonify({'message': f'Se elimino la criptomoneda {crypto_code}'})
        return jsonify({'error': f'La criptomoneda {crypto_code} no se encontró'}), 404

@app.route('/politicas-y-terminos-de-uso')
def getpoliticasyterminosdeuso():
    return jsonify({'Politicas y Terminos de Uso': politicasyterminosdeuso, 'Reglas':reglas})
    
@app.route('/politicas-de-privacidad', methods=['GET', 'PUT'])
def get_or_update_politicas_de_privacidad():
    if request.method == 'GET':
        return jsonify({
            'Politicas de Privacidad': politicasdeprivacidad,
            'Info. que recopilamos': informacionquerecopilamos,
            "Uso de la info.": usodelainformacion,
            "Compartir info.": compartirinformacion,
            "Seguridad de datos": seguridaddedatos,
            "Cookies": cookiesytecnologiassimilares,
            "Cambios en la politica de privacidad": cambiosenlapoliticadeprivacidad,
            "Contacto": contacto
        })
    
    elif request.method == 'PUT':
        data = request.get_json()
        nuevo_contacto = data.get("Contacto")
        contacto[0] = nuevo_contacto
        return jsonify({
            'Politicas de Privacidad': politicasdeprivacidad,
            'Info. que recopilamos': informacionquerecopilamos,
            "Uso de la info.": usodelainformacion,
            "Compartir info.": compartirinformacion,
            "Seguridad de datos": seguridaddedatos,
            "Cookies": cookiesytecnologiassimilares,
            "Cambios en la politica de privacidad": cambiosenlapoliticadeprivacidad,
            "Contacto": contacto
        })

@app.route('/donaciones', methods=['GET'])
def getdonaciones():
    return jsonify ({'donaciones': donaciones})

@app.route('/form', methods=['GET', 'POST'])
def mostrar_formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        variedad = request.form['variedad']

        donacion = {'nombre': nombre, 'cantidad': cantidad, 'variedad': [variedad]}

        if variedad == "dinero":
            opcionesDinero = request.form['opcionesDinero']
            donacion['opcionesDinero'] = opcionesDinero
        elif variedad == "cryptos":
            opcionesCryptos = request.form['opcionesCryptos']
            donacion['opcionesCryptos'] = opcionesCryptos

        donaciones.append(donacion)

        return redirect(url_for('confirmacion'))

    return render_template('formulario.html')


@app.route('/confirmacion', methods=['POST'])
def recibir_confirmacion():
    data = request.get_json()
    mensaje = data.get("mensaje")
    return "Gracias por tu donación. " + mensaje

if __name__ == '__main__':
    app.run(debug=True, port=4000)
