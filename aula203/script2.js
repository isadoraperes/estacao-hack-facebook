//programa que avalie o empréstimo
//idade do usuário, qtd dinheiro, qto ganha/mês
//regras:
//entre 22 e 55 anos
//valor a partir de 1k
//valor NÃO pode ser maior que 15x > ganha/mês
//resposta: aceito ou não aceito
//perguntar qtd parcelas (3 a 20 vezes) e calcular juros compostos de 8%/mês
//retornar valor total do emprestimo e valor da parcela

// let nome = prompt('Olá, qual o seu nome?');
// let idade = Number(prompt('Informe sua idade:'));
// let valorEmprestimo = Number(prompt('Qual o valor de empréstimo que você precisa?'));
// let salario = Number(prompt('Qual o valor do seu salário?'));

function calcularEmprestimo(nome, idade, valorEmprestimo, salario, qtdParcelas) {
    if (idade < 22 || idade > 55) {
         console.log(`${nome}, infelizmente o seu empréstimo não foi aceito.`);
    } else if (Number(valorEmprestimo) > (15*salario)) {
        console.log(`${nome}, infelizmente o seu empréstimo não foi aceito.`);
    } else if (Number(valorEmprestimo) < 1000) {
        console.log(`${nome}, por favor, digite um valor acima de R$1000,00.`);
    } else {
        if (qtdParcelas < 3 || qtdParcelas > 20) {
            console.log(`${nome}, por favor, digite a quantidade de parcelas entre o míninmo de 3 parcelas e máximo de 20 parcelas`);
        } else {
            let jurosCompostos = (valorEmprestimo * Math.pow((1 + (8/100)), qtdParcelas)).toFixed(2);
            let valorParcelas = (jurosCompostos / qtdParcelas).toFixed(2);
            console.log(`Parabéns, ${nome}! Seu empréstimo foi aceito! O valor das suas ${qtdParcelas} parcelas é de R$${valorParcelas}. Totalizando R$${jurosCompostos} de empréstimo com 8% de juros compostos.`);
        }
    }
}

//exercicio


//o usuario vai digitar a idade dele e a função tem que retornar quais os filmes que ele pode ver
// dica: é preciso usar loop (for)

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

function classificarFilme(idade) {

    let listaFilmes = [];

    for (let index = 0; index < filmes.length; index++) {
        if (idade >= filmes[index].classificacao) {
           console.log(filmes[index].titulo);
           listaFilmes.push(filmes[index].titulo); 
        }
    }

    if (listaFilmes.length == 0) {
        console.log('Em breve adicionaremos um filme no catálogo para você.');
    } else {
        console.log(`Você pode assistir aos seguintes filmes: ${listaFilmes}`);
    }    
}
    