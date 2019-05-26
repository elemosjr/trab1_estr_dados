#!/bin/python

## Exercício 1.8
import re

def main():
  valor = int(input("Qual o valor? "))

  notas_valor(valor)


def notas_valor(valor):
  resto = valor
  quant = []
  nota = [100,50,10,5,2,1]

  for i in nota:
    quant.append(int(resto/i))
    resto = valor%i
    if resto == 0:
      break
  
  quant = quant+list(map(int, list("0"*(6-len(quant)))))

  quant.reverse()

  nota.reverse()

  text_nota = ""

  interval = list(range(0, len(nota)))

  for i in interval:
    if quant[i] == 0:
      pass
    elif quant[i] == 1:
      text_nota = text_nota+", "+str(quant[i])+" nota de "+str(nota[i])
    else:
      text_nota = text_nota+", "+str(quant[i])+" notas de "+str(nota[i])

    if quant[i] == 0:
      pass
    elif nota[i] == 1:
      text_nota+" real"
    else:
      text_nota+" reais"

  result = "A menor combinação possível de notas para dar o valor R$"+str(valor)+" é "+re.sub("^,\ ", "", text_nota)

  print(result)


if __name__ == "__main__":
  main()
