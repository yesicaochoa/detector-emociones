from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

vectorizer, modelo = joblib.load('modelo.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    emocion = ''
    if request.method == 'POST':
        frase = request.form.get('frase', '')
        if frase:
            X = vectorizer.transform([frase])
            emocion = modelo.predict(X)[0]
    return render_template('index.html', emocion=emocion)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
