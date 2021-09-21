'''
Exercise nº1 - Class 2 - Python Basic

Faça um programa que leia o Nome, Idade, Altura, CPF, Número de Telefone e
endereço residencial. E organize todas as informações em um relatório de texto
e em seguida uma lista dos dados enviados.

'''

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

print('\nO cliente', nome, 'de',  idade, 'anos, titulado com o nº de CPF', cpf + ', passou durante o exame de altura de corpo.')
print('Possuindo uma estrutura corporal de aproximadamente', altura, 'metros de altura, fez que conseguisse ganhar a aprovação na mesa de jurados.')
print('Por gentileza entregar o resultado por meio do corrio para o endereço', endereco + '. Juntamente, o envio da notificação por meio do telefone', telefone + '.')

print('\n\nNome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('CPF: ', cpf)
print('Telefone: ', telefone)
print('Endereço: ', endereco)