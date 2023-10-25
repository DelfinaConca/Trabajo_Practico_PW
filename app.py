from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from cryptos import cryptos
from donaciones import donaciones

@app.get("/")
def home():
    return render_template ("home.html")

@app.route('/cryptos')
def getcryptos():
    return jsonify({'cryptos': cryptos})


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
