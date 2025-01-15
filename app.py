from flask import Flask, render_template
from palavras import lista_palavras
import random

app = Flask(__name__)

@app.route("/")
def index():
    palavra = random.choice(lista_palavras)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)