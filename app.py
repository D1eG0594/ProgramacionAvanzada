from flask import Flask, render_template, request
from formas import Cuadrado, Circulo, Triangulo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    forma = request.form.get("forma")
    if forma == "cuadrado":
        lado = float(request.form.get("lado"))
        if not lado:
            return render_template("index.html")
        cuadrado = Cuadrado(lado)
        area = round(cuadrado.area(), 2)
        perimetro = round(cuadrado.perimetro(), 2)
        return render_template("resultado.html", area = area, perimetro = perimetro, froma=forma)
    elif forma == "circulo":
        radio = float(request.form.get("radio"))
        if not radio:
            return render_template("index.html")
        circulo=Circulo(radio)
        area = round(circulo.area(), 2)
        perimetro = round(circulo.perimetro(), 2)
        return render_template("resultado.html", area = area, perimetro = perimetro, forma = forma)
    elif forma == "triangulo":
        base = float(request.form.get("base"))
        altura = float(request.form.get("altura"))
        lado1 = float(request.form.get("lado1"))
        lado2 = float(request.form.get("lado2"))
        lado3 = float(request.form.get("lado3"))
        if base and altura and lado1 and lado2 and lado3:
            triangulo = Triangulo(base, altura, lado1, lado2, lado3)
            area = round(triangulo.area(), 2)
            perimetro = round(triangulo.perimetro(), 2)
            return render_template("resultado.html", area = area, perimetro = perimetro, forma = forma)
    else:
        return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True, port=5000)