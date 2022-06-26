# Faça um programa que leia pelo teclado e mostre na tela o seu tipo primitivo, e todas as informaçoes possíveis sobre ele:
# Se ele é um número, uma letra, se é inteiro, com ponto flutuante... e assim por diante.

variavel = input("Digite algo: ")
print(f'Essa variável é um letra ou número? {variavel.isalnum()}\n'
      f'É uma letra? {variavel.isalpha()}\n'
      f'É um número? {variavel.isdigit()}\n'
      f'É um caractere especial? {variavel.isascii()}\n'
      f'É um decimal? {variavel.isdecimal()}\n'
      f'É um identificador? {variavel.isidentifier()}')
