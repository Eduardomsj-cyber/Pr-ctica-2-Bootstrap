from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Aquí se valida la información de usuario con la base de datos
        if username == "usuario" and password == "contraseña":
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrecta")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
