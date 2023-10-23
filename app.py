from flask import Flask, jsonify, request

app = Flask(__name__)

from cryptos import cryptos

@app.route('/cryptos')
def getcryptos():
    return jsonify({'cryptos': cryptos})



if __name__ == '__main__':
    app.run(debug=True, port=4000)
