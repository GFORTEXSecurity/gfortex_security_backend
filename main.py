from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel: Ein einfacher API-Endpunkt
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hallo, das ist dein Backend!"})

# Beispiel: Ein API-Endpunkt mit JSON-Daten
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json  # JSON-Daten von der App empfangen
    return jsonify({"received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)