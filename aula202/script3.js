// //exercicio
// construir uma escada com # e tem que ser com 5 degraus
// necessário usar: laço e console.log
// # 
// ##
// ###
// ####
// #####

// let escada = [];
// let material = '#';
// let degrau = '';

// for (let index = 0; index < 5; index++) {
//     degrau += material;
//     escada.push(degrau);
// }
// console.log(escada);

// for (let degrau of escada) {
//     console.log(degrau);
// }

console.log('=======');


//perguntar pro usuario qual o material da escada e quantos degraus tem a escada

let escada = [];
let material = prompt('Digite o material desejado:');
let qtd = Number(prompt('Digite a quantidade de degraus desejada:'));
let degrau = '';

for (let index = 0; index < qtd; index++) {
    degrau += material;
    escada.push(degrau);
}
console.log(escada)

for (let degrau of escada) {
    console.log(degrau);
}


