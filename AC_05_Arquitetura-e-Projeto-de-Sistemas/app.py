# app.py

import os
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import *

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cliente = Cliente(request.form['nome'],
                          request.form['email'],
                          request.form['cpf'])
        db.session.add(cliente)
        db.session.commit()
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
