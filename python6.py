#!/usr/bin/env pyhton3
with open("python6.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.upper()
        print(linha)
