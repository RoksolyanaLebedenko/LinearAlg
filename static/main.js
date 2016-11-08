document.addEventListener("DOMContentLoaded",ready);

function ready(){
var btn = document.querySelector('.submit-size');
btn.addEventListener('click', createMatrix);
}

function createMatrix() {
var form = document.querySelector('.created-matrix');
var columnSize = document.querySelector('.column-size').value;
var rowSize = document.querySelector('.row-size').value;
console.log(columnSize);
var matrix = document.createElement("form");
matrix.className = "column-row";

for (var i = 0; i < columnSize*rowSize; i++) {
if (i % rowSize == 0) {
matrix.innerHTML += "<input type='number' name='matrix-elem' class='elem first-elem'>";
}
else {
matrix.innerHTML += "<input type='number' name='matrix-elem' class='elem'>";


}
}
matrix.innerHTML += "<div id='computation-choice'><div class='computation-variant'><label for='l-u-factorization'><b>Solve Ax = b via LU-factorization</b></label><input type='submit' name='LUFactorization' id='l-u-factorization' value='Calculate'></div></div>";
form.appendChild(matrix);
}