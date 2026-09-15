const inputs = document.querySelectorAll (".required");
const spans = document.querySelectorAll (".span-required");
function passwordValidate() {
    if (inputs[0].value.length>=8 && inputs[0]==inputs[1]) {
        setError(0); 
        console.log ("Senhas devem ser iguais e ter no mínimo 8 caracteres");
        
    }
    else {
        removeError(0);
        console.log ("Validado com sucesso");
    }
}

function setError(index) {
    spans[index].style.display = "block"
}

function removeError(index) {
    spans[index].style.display = "none";
}