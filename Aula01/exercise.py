# 🚀 Exercício 1:
# Crie uma função que receba dois números e retorne o maior deles.

def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(maior_numero(10, 5))   # 10


# 🚀 Exercício 2:
#  Calcule a média aritmética dos valores contidos em uma lista.

import random

list_num = random.sample(range(1, 100), 20)

print(list_num)

size = len(list_num)

print(size)

total = sum(list_num)

print(total)

media = total / size

print(media)


# 🚀 Exercício 3:
# Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.

def quadrado(n):
    for i in range(n):
        print('*' * n)


quadrado(5)


# 🚀 Exercício 4:
# Crie uma função que receba uma lista de nomes
# e retorne o nome com a maior quantidade de caracteres.

list_names = ["José", "Lucas", "Nádia",
              "Fernanda", "Cairo", "Joana",
              "Camilo", "Washington"]


def find_longest_name(names):
    # Usamos a função max com a chave len para encontrar o nome mais longo
    longest_name = max(names, key=len)
    return longest_name


print(find_longest_name(list_names))
