from flask import Flask, render_template, request  #Se importa flask
from objetos import ContactoPersona, SaludPersona  #Se importan los objetos



persona = ContactoPersona("Juan", 123456789, "hola@gmail.com")

persona = SaludPersona("Juan", 123456789, "hola@gmail.com","hoy", "60Kg", "180cm", "Bajar de peso", "Ninguna")

print(persona.nombre)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")   #Se renderiza la pagina principal



@app.route("/rutina", methods=["POST"])
def rutina():

    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    return render_template("llegada.html")






if __name__=="__main__":
    app.run(debug=True, port=5000)