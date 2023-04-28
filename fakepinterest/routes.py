from flask import Flask, render_template, url_for
from flask_login import login_required
from fakepinterest import app 


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario, idade=25)