# Operadores Aritiméticos

# Centralizar string utilizar ":^20"
# orientar a esquerda utilizar ":<30" ou a direita ":>40"

nome = input("Digite um nome: ").title()
print(f'Seja bem vindo {nome:=^20}')
# formatar casas decimais utilizar ":.2f" para formatar 2 casas decimais.
# pular uma linha utilizar "/n"
# para voltar uma linha utilizar |=end""|
# DwkS

# Operadores aritiméticos por ordem de precedência.
# () parenteses {Tudo será resolvido primeiro dentro dos parenteses}
# ** potenciação
# % resto da divisão
# // divisão inteira
# * multiplicação / divisão
# + soma - subração

n1 = input("Digite o primeiro número: ")
n2 = input("Ditite o segundo número: ")
n3 = int(n1)  # transforma a string digitada em numero inteiro
n4 = float(n2)  # transforma a string digitada em número flutuante

concatenacao = n1 + n2
soma = n3 + n4
subtracao = int(n1) - int(n2)
multiplicacao = n3 * n4
divisao = n3 / n4
potenciacao = n3 ** n4
divisaoInteira = n3 // n4
restodivisao = n3 % n4
exprecao = n3 + n4 * n3 / (n3 + n3 - (n4 + 1)) ** 2
print(
    f"\nA concatenação de {n1} + {n2} é {concatenacao}\n"
    f"A soma entre {n1} e {n2} é: {soma}\n"
    f"A subtação entre {n1} e {n2} é: {subtracao}\n"
    f"A multiplicação entre {n1} e {n2} é: {multiplicacao}\n"
    f"A divisão de {n1} por {n2} é: {divisao:.2f}\n"
    f"A potenciação de {n1} elevado a {n2} é: {potenciacao}\n"
    f"A divisão inteira de {n1} por {n2} é: {divisaoInteira:.0f}\n"
    f"O resto da divisão de {n1} por {n2} é : {restodivisao:.0f}\n"
    f"E o valor da expressão numérica {n1} + {n2} * {n1} / ({n1} + {n1} - ({n2} + 1)) ** 2 é : {exprecao:.3f}")
