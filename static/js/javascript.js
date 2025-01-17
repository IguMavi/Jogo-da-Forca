document.addEventListener("DOMContentLoaded", () => {
    atualizarboard();
});

// --------------- //

const input = document.getElementById("tentativa");

document.getElementById("form-tentativa").addEventListener("submit", function (event) {
    event.preventDefault();
    verificar_tentativa();
    input.value = "";
});

// ----------------- //

function atualizarboard() {
    const board = document.getElementById("board");
    board.innerHTML = ""; // para limpar o conteudo e atualizar o jogo
    
    fetchPalavra().then((palavra) => {
        let palavra_secreta = new Array(palavra.length).fill("_");

        palavra_secreta.forEach(letra => {
            let letraConteudo = document.createElement("h1");
            letraConteudo.textContent = letra;
            board.appendChild(letraConteudo);
        });
    });
};


// funcao q recebe a palavra gerada
const fetchPalavra = () => {
    fetch("http://127.0.0.1:5000/get_palavra", {
        method: "GET",
    })
    .then((response) => response.json())
    .then((data) => {
        dados = data;
    })
};
 
// funcao q comunica com o back para verificar a letra
async function fetchData(letra){
    const response = await fetch("http://127.0.0.1:5000/verificar-tentativa", {
        method: "POST",     // tipo de requisição
        headers: {
            'Content-Type': 'application/json' // Tipo de conteúdo enviado
          },
        body: JSON.stringify({
            tentativa: letra,
        })  
    });

    return await response.json()
}

// funcao q ativa a outra e muda o front
async function verificar_tentativa() {
    var letra = document.getElementById("tentativa").value;
    const response = await fetchData(letra);

    fetchData().then((palavra) => {
        let palavra_secreta = new Array(palavra.length).fill("_");

        if (response.posicao === "errou") {
            console.log("sla ne")
        }else if (response.posicao) {
            response.posicao.forEach(pos => {
                palavra_secreta[pos] = letra
            });
        };
    });

    atualizarboard();
};   