from django.db import models

# Create your models here.
# as classes serão criadas aqui

# code first - fazer o código primeiro e depois gerar o bd em uma aplicação
# python utiliza o code first

# o models é a herança de tudo que tem de Model no django
class Pessoa(models.Model):
    nome = models.CharField(
        max_length = 255,
        verbose_name = 'Nome'
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name = 'Sobrenome'
    )

    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        #lado esquerdo - como fica salvo no bd
        #lado direito - como mostra para o usuário
    )

    sexo = models.CharField(
        max_length = 255,
        verbose_name = 'Sexo',
        choices = SEXOS
    )

    email = models.EmailField(
        max_length = 255,
        verbose_name = 'E-mail',
        blank = False
    )

    biografia = models.TextField(
        null = True,
        blank = True
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    #retorna uma string
    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    
    
