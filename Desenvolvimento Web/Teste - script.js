const inputs = document.querySelectorAll (".required");
const spans = document.querySelectorAll (".span-required");
function nameValidate() {
    if (inputs[0].value.length<3) {
        setError(0); 
        console.log ("Nome deve ter 3 caracteres");
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