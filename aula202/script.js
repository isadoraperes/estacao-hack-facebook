// desafio:
// login
// caso usuario digite o login e senha corretos, msg 'login efetuado com sucesso'
// se o usuario digitar o login errado, msg 'login inválido'
// se o usuario digitar a senha errada, msg 'senha incorreta'

let user = 'isadora'
let pass = 'teste123'

if (user == 'isadora' && pass == 'teste123') {
    console.log('Login efetuado com sucesso');
} else if (user != 'isadora') {
    console.log('Login inválido');
} else if (senha != 'teste123') {
    console.log('Senha incorreta');
}

let userPage = prompt('Digite seu login');
let passwordPage = prompt('Digite sua senha');

if (userPage == user && passwordPage == pass) {
    alert('Login efetuado com sucesso');
} else if (userPage != user) {
    alert('Login inválido');
    alert('Login inválido');
} else if (passwordPage != pass) {
    alert('Senha incorreta');
}

