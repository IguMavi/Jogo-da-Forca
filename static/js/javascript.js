const input = document.getElementById("tentativa");

document.getElementById("form-tentativa").addEventListener("submit", function (event) {
    event.preventDefault();
    verificar_tentativa();
    input.value = "";
});

// ----------------- //

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

async function verificar_tentativa() {
    var letra = document.getElementById("tentativa").value;
    const response = await fetchData(letra);

    if (response.response === true) {
        console.log("acertou")
    } else {
        console.log("errou")
    }
}   