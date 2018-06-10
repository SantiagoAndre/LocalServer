from flask import Flask
from flask import render_template
from flask import request

from forms import FormVotacion

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form_votacion = FormVotacion(request.form)
    if request.method == 'POST':
        if form_votacion.validate():
            print('Valor id persona:', form_votacion.id_persona.data)
            print('Valor checkbox:', request.form.get('votar'))

            form_votacion = FormVotacion()
            return render_template('index.html', form = form_votacion)
    return render_template('index.html', form = form_votacion)

if __name__ == '__main__':
    app.run(debug = True)
