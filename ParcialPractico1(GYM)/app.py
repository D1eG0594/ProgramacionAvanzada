from flask import Flask, render_template, request  #Se importa flask
from objetos import Cliente  #Se importan los objetos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")   #Se renderiza la pagina principal


@app.route("/registrar_cliente", methods=["POST"])
def rutina():

    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    email = request.form.get("email")
    fecha_nacimiento = request.form.get("fecha_nacimiento")
    peso = request.form.get("peso")
    altura = request.form.get("altura")
    objetivo = request.form.get("objetivo")
    condiciones_medicas = request.form.get("condiciones_medicas")
    
    #Se crea el objeto con los datos obtenidos
    usuario = Cliente(nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas) 

    rutina_asignada = usuario.asignar_rutina()  # Llama al método asignar_rutina()


    return render_template("llegada.html", usuario = usuario, rutina = rutina_asignada)


if __name__=="__main__":
    app.run(debug=True, port=5000)