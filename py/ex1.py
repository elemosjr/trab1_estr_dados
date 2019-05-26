#!/bin/python

## Exercício 1
import re

def main():
  val_nota = [1,2,5,10,50,100]
  
  notas = list(range(0, len(val_nota)))

  notas[0] = int(input("Quantas notas de 1 real tem no monte? "))

  for i in list(range(1, len(val_nota))):
    notas[i] = int(input("Quantas notas de "+str(val_nota[i])+ " reais tem no monte? "))

  valor_notas(notas)


def valor_notas(notas):
  val_nota = [1,2,5,10,50,100]
  valor = 0

  interval = list(range(0, len(val_nota)))

  for i in interval:
    valor = valor+(notas[i]*val_nota[i])

  text_nota = ""

  for i in interval:
    if notas[i] == 0:
      pass
    elif notas[i] == 1:
      text_nota = text_nota+", "+str(notas[i])+" nota de "+str(val_nota[i])
    else:
      text_nota = text_nota+", "+str(notas[i])+" notas de "+str(val_nota[i])

    if notas[i] == 0:
      pass
    elif val_nota[i] == 1:
      text_nota = text_nota+" real"
    else:
      text_nota = text_nota+" reais"

  result = re.sub("^,\ ", "", text_nota)+" dão um total de R$"+str(valor)+" reais."

  print(result)


if __name__ == "__main__":
  main()
