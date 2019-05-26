#!/bin/python

## Exercício 2.7
import pandas as pd
import numpy as np

def main():
  valor = float(input("Qual o valor? "))

  juros(valor)


def juros(valor):
  parcelas = [1, 3, 6, 9, 12]
  total_juros = np.array([1.0, 1.1, 1.15, 1.2, 1.25])*valor

  df = pd.DataFrame({"Valor da Divida":total_juros,
                     "Valor dos Juros":total_juros-valor,
                     "Quantidade de Parcelas":parcelas,
                     "Valor da Parcela":total_juros/parcelas})

  print(df)


if __name__ == "__main__":
  main()
