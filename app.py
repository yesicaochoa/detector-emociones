from flask import Flask, request, render_template, jsonify
import joblib
import os

app = Flask(__name__)

vectorizer, modelo = joblib.load('modelo.joblib')

@app.route('/')
def home():
    return "API para detección de emociones."

@app.route('/api/detectar', methods=['POST'])
def detectar():
    frase = request.form['frase']
    X = vectorizer.transform([frase])
    emocion = modelo.predict(X)[0]
    return jsonify({'emocion': emocion})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
