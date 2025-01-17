from flask import Flask, render_template, request
from palavras import palavra_secreta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", palavra = palavra_secreta)

@app.route("/get_palavra", methods=["GET"])
def get_palavra():
    tamanho = len(palavra_secreta)
    return {"palavra": palavra_secreta, "tamanho": tamanho}

@app.route("/verificar-tentativa", methods=["POST"])
def verificacao():
    data = request.get_json()
    tentativa = data.get("tentativa")
    
    if tentativa in palavra_secreta:
        acertos = []
        for posicao in range(len(palavra_secreta)):
            if tentativa == palavra_secreta[posicao]:   
                acertos.append(posicao)
        return {"posicao": acertos}
    else:
        return {"posicao": "errou"}

if __name__ == "__main__":
    app.run(debug=True)