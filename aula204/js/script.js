//explicando os diferentes tipos de for
let numeros = [5, 7, 9, 0];
let pessoa = {
    nome: 'Isadora',
    idade: 25,
    cpf: '999.999.999-09',
    rg: '66.666.666-6'
};

for (let index = 0; index < numeros.length; index++) {
    console.log(numeros[index]);
}

for (let atributo in pessoa) {
    console.log(pessoa[atributo])
}

let filmes = [
    {
        titulo: 'Harry Potter', 
        classificacao: 12
    },
    {
        titulo: 'As branquelas',
        classificacao: 16
    },
    {
        titulo: 'Rei Leão',
        classificacao: 10
    },
    {
        titulo: 'Interestelar',
        classificacao: 10
    },
    {
        titulo: 'Ninja Assassino',
        classificacao: 18
    },
    {
        titulo: 'John Wick',
        classificacao: 16
    },
    {
        titulo: 'Velozes e Furiosos',
        classificacao: 14
    }
];

let idade = Number(prompt('Digite sua idade:'));

//itera valores
for (let filme of filmes) {
    if(idade >= filme.classificacao) {
        console.log(filme.titulo);
    }
}

//itera indices
for (let indice in filmes) {
    if (idade >= filmes[indice].classificacao) {
        console.log(filmes[indice].titulo);
    }
}