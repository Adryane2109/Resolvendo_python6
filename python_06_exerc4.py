#!/usr/bin/env python3

numero_linhas = 0
numero_caracteres = 0

with open("Python_06.fastq", "r") as arquivo:
    for linha in arquivo:
        numero_linhas += 1
        numero_caracteres += len(linha)

media = numero_caracteres / numero_linhas

print("Número total de linhas:", numero_linhas)
print("Número total de caracteres:", numero_caracteres)
print("Comprimento médio da linha:", media)
