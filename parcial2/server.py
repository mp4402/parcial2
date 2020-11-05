from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json
import yaml 

file_loader = FileSystemLoader("templates")
env = Environment(loader = file_loader)

app = Flask(__name__)

output = [""]

def reverse(cadena):
    for n in cadena:
        nCadena = n + nCadena
    output[0] = nCadena

def longitud(cadena):
    largoCadena = len(cadena)
    output.append(largoCadena)

def vowelsConsonants(cadena):
    vocal = 0
    consonante = 0
    carAsc = 0
    vocales = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    consonantes = [66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]
    for n in cadena:
        carAsc = ord(n)
        for m in vocales:
            if carAsc == m:
                vocales += 1

        for m in consonante:
            if carAsc == m:
                consonante += 1
    
    output.append(vocales)
    output.append(consonante)

def upper(cadena):
    upCadena = cadena.upper()
    output.append(upCadena)

def lower():
    pass

def upDown():
    pass

def naive():
    pass

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        _input = request.form['input']
        return redirect(url_for("index"))
    template = env.get_template("index.html")
    return template.render()

@app.route("/crear", methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        _id = request.form["id"]
        _type = request.form["type"]
        _name = request.form["name"]
        _quantity = request.form["quantity"]
        
        my_json["data"].append({"id":_id,"type":_type,"name":_name,"quantity":_quantity})
        return redirect(url_for("index"))

    template = env.get_template("form.html")
    return template.render()

if __name__ == "__main__":
    app.run()