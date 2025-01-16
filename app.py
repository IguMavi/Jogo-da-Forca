from flask import Flask, render_template, request
from palavras import palavra_secreta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", palavra = palavra_secreta)

@app.route("/verificar-tentativa", methods=["POST"])
def verificacao():
    data = request.get_json()
    tentativa = data.get("tentativa")

    if tentativa in palavra_secreta or tentativa == palavra_secreta:
        return {"response": True}
    return {"response": False}

if __name__ == "__main__":
    app.run(debug=True)