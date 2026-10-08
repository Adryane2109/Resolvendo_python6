#!/usr/bin/env python3
sequencias = {}
nome = ""
sequencia = ""

with open("arquivo_fasta.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.rstrip()

        if linha.startswith(">"):
            if nome:
                sequencias[nome] = sequencia

            nome = linha[1:]
            sequencia = ""

        else:
            sequencia += linha

    sequencias[nome] = sequencia
print(sequencias)
