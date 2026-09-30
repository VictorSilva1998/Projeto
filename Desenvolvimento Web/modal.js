var modal = document.getElementById ("modal");
var abrir = document.getElementById ("abrir");
var fechar = document.getElementById ("fechar");

abrir.addEventListener ("click", function() {
    modal.style.display = "block";
});

fechar.addEventListener ("click", function() {
    modal.style.display = "none";
});