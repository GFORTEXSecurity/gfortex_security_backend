from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render erwartet einen offenen Port
    app.run(host='0.0.0.0', port=port)