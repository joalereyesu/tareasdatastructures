from flask import Flask, render_template, request, url_for, redirect
import functions

app = Flask(__name__)

@app.route("/")
def start():
    return "Hola!"

@app.route("/linear/<int:N>/<int:value>", methods = ["GET"])
def startLinearSearch(N, value):
    lista = functions.CreateList(N)
    if functions.linearSearch(lista, value) == True:
        return f"Busqueda Lineal:\nEl valor {value} si se encuentra en la lista"
    else: 
        return f"Busqueda Lineal:\nEl valor {value} no se encuentra en la lista"

@app.route("/binary/<int:N>/<int:value>", methods = ["GET"])
def startBinarySearch(N, value):
    lista = functions.CreateList(N)
    if functions.binarySearch(lista, 0, (len(lista)-1), value) == True:
        return f"Busqueda Binaria:\nEl valor {value} si se encuentra en la lista"
    else: 
        return f"Busqueda Binaria:\nEl valor {value} no se encuentra en la lista"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
