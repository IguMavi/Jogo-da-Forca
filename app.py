from flask import Flask, render_template
from palavras import lista_palavras
import random

app = Flask(__name__)

@app.route("/")
def index():
    palavra = random.choice(lista_palavras)
    tamanho = len(palavra)
    return render_template("index.html", palavra = palavra, tamanho = tamanho)

if __name__ == "__main__":
    app.run(debug=True)