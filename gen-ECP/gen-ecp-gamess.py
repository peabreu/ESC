#!/usr/bin/python
import sys
filename = sys.argv[-1]
print(filename)
ficheiro = open(filename)
basis = ""
while True:
  linha = ficheiro.readline()
  print(str(linha))
  if str(linha)[0:6] == " $DATA":
    break
ficheiro.readline()
ficheiro.readline()
linhas = ficheiro.readlines()
for l in linhas:
  symb = l.split()[0]
  if symb == "$END":
    break
  linha = symb + "-ecp none"
  print(linha)
  basis = basis + "bas" + symb + ", "
print(basis)
ficheiro.close()
