from flask import Flask, render_template, request
from objetos import Cliente
import sqlite3

app = Flask(__name__)


def crear_tabla_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        telefono TEXT,
                        email TEXT,
                        fecha_nacimiento DATE,
                        peso REAL,
                        altura REAL,
                        objetivo TEXT,
                        condiciones_medicas TEXT
                    )''')
    conn.commit()

def insertar_usuario(conn, usuario):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO usuarios (nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (usuario.nombre, usuario.telefono, usuario.email, usuario.fecha_nacimiento, usuario.peso, usuario.altura, usuario.objetivo, usuario.condiciones_medicas))
    conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

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
    
    usuario = Cliente(nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas) 

    rutina_asignada = usuario.asignar_rutina()


    conn = sqlite3.connect('usuarios.sqlite')
    cursor = conn.cursor()
    crear_tabla_usuarios(conn)
    insertar_usuario(conn, usuario)
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    

    return render_template("llegada.html", usuario=usuario, rutina=rutina_asignada)

if __name__ == "__main__":
    app.run(debug=True, port=5000)