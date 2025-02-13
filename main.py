from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

@app.route('/api/hello'), methods=['GET'])
def hello():
    return jsonify({"message": "Hallo, das ist dein Backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)