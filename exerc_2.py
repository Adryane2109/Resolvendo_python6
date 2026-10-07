#!/usr/bin/env python3
with open("python6.txt", "r") as arquivo:
    with open("Python_06_uc.txt", "w") as novo_arquivo:
        for linha in arquivo:
            linha = linha.upper()
            novo_arquivo.write(linha)
