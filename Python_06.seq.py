#!/usr/bin/env python3
with open("Python_06.seq.txt", "r") as arquivo:
    for linha in arquivo:
        nome, sequencia = linha.rstrip().split("\t")

        complemento = sequencia.translate(str.maketrans("ATCG", "TAGC"))
        reverso = complemento[::-1]

        print(">" + nome + " complemento reverso")
        print(reverso)
