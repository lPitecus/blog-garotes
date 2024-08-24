from django.db import models

# Create your models here.
# Cada classe representa uma tabela dentro do aplicativo polls, onde cada coluna eh um elemento dentro dessa classe.
# Essa classe representa as perguntas dentro da plataforma.
class Question(models.Model):
    # Essa coluna ou campo representa o texto da pergunta. Definido como um campo de caracteres (CharField) com limite
    # de 200 caracteres.
    question_text = models.CharField(max_length=200)
    # Esse campo representa a data de publicação da pergunta. O nome da variável está em formato "machine-friendly", se
    # o dev desejar, pode mudar o nome para um formato "human-readable" passando como primeiro parâmetro, em qualquer
    # campo, o nome nesse novo formato para ajudar na leitura.
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    # Esse campo cria um relacionamento many-to-one com a tabela Question através do metodo ForeignKey. Ou seja, cada
    # escolha é relacionada com uma única pergunta.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Esse campo possui um argumento obrigatório devido o uso do metodo CharField.
    choice_text = models.CharField(max_length=200)
    # Já o metodo IntegerField recebe um argumento opcional, que deixa o valor padrão dele como 0.
    votes = models.IntegerField(default=0)

