from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/submit", methods=["POST"])
def submit():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    experiencia = request.form["experiencia"]
    comentarios = request.form["comentarios"]
    
    with open("respuestas.csv", "a") as file:
        file.write(f"{nombre},{correo},{telefono},{experiencia},{comentarios}\n")
    
    return "¡Gracias por inscribirte en el torneo!"

if __name__ == "__main__":
    app.run(debug=True)