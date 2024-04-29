from flask import Flask, render_template, request, jsonify
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
    
    # Crear objeto Cliente
    usuario = Cliente(nombre, telefono, email, fecha_nacimiento, peso, altura, objetivo, condiciones_medicas) 

    # Asignar rutina al usuario
    rutina_asignada = usuario.asignar_rutina()

    # Conexión a la base de datos
    conn = sqlite3.connect('usuarios.sqlite')
    cursor = conn.cursor()

    # Crear tabla de usuarios si no existe
    crear_tabla_usuarios(conn)

    # Insertar usuario en la base de datos
    insertar_usuario(conn, usuario)




    #cursor.execute("SELECT * FROM usuarios")
    #rows = cursor.fetchall()
    #for row in rows:
        #print(row)


    conn.close()
    

    return render_template("llegada.html", usuario=usuario, rutina=rutina_asignada)


@app.route("/tabla_usuario")
def tabla_usuario():
    conn = sqlite3.connect('usuarios.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, telefono, email FROM usuarios")
    usuarios = cursor.fetchall()
    
    conn.close()
    return render_template("tabla_usuario.html", usuarios=usuarios)


# Ruta para cargar los usuarios desde la base de datos
@app.route("/api/usuarios")
def obtener_usuarios():
    conn = sqlite3.connect('usuarios.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, telefono, email FROM usuarios")
    usuarios = cursor.fetchall()
    print(usuarios)
    conn.close()
    return jsonify({"usuarios": usuarios})

@app.route("/api/editar_usuario/<int:usuario_id>", methods=["POST"])
def editar_usuario(usuario_id):
    conn = sqlite3.connect('usuarios.sqlite')
    cursor = conn.cursor()

    data = request.json  # Obtener los datos enviados por el cliente

    # Actualizar los datos del usuario en la base de datos
    cursor.execute('''UPDATE usuarios 
                      SET nombre=?, telefono=?, email=?
                      WHERE id=?''',
                   (data['nombre'], data['telefono'], data['email'], usuario_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Usuario actualizado correctamente"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)