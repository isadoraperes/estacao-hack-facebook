// while -> codigo se repete enquanto a condição for verdadeira

let signos = ['aries', 'touro', 'gemeos', 'cancer', 'leão', 'virgem', 'libra', 'escorpião', 'sagitário', 'capricórnio', 'aquario', 'peixes'];

// console.log(signos);

let contador = 0;

while (contador < 5) {
    console.log(contador);
    contador++;
}

let cont = 0;
while (cont < 12) {
    console.log(signos[cont]);
    cont++;
}

console.log('==============');

for (let index = 0; index < signos.length; index++) {
    console.log(signos[index]);
}

// não sabemos quantas vezes o usuario pode errar
// então utilizamos o while
// let idade = Number(prompt('Digite a sua idade'));
// while (isNaN(idade)) {
//     alert('POr favor, digite um número');
//     idade = Number(prompt('Digite a sua idade'));
// }

console.log('==============');

//itera e percorre todos os indices da lista
//somente funciona para listas!
for(let i in signos) {
    console.log(i);
}

console.log('==============');

//o que é o indice no for:in, no for:of é o elemento em si, presente dentro do indice que está sendo percorrido no momento
// for (const iterator of object) {
//     iterator == object[index.value]
// }
for (let signo of signos) {
    console.log(signo);
}

console.log('==============');