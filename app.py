from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/cryptos')
def cryptos():
    return jsonify({'cryptos': cryptos})

@app.route('/cryptos')
def cryptos():
    return "Bienvenido a DonaOnline"

if __name__ == '__main__':
    app.run(debug=True, port=4000)
