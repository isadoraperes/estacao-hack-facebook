function somar(number1=0, number2=0) {
    return Number(number1 + number2);
}

function printEscada(material, degrau) {
    let escada = material;
    for (let index = 0; index < degrau; index++) {
        console.log(escada);
        escada += material;
    }
}

function oddNumber(number) {
    if (number %2 == 0) {
        return 'O número é par';
    } else {
        return 'O número é ímpar';
    }
}

//função que gere numeros inteiros aletórios

const aletorio = function (minIntervalo, maxIntervalo) {
    return Math.floor(Math.random()*(maxIntervalo - (minIntervalo + 1)) + minIntervalo);
}

//(10 - 2) -> 8
//(8 + 2) -> 10
// 10