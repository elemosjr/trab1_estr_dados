#!/bin/python

## Exercício 2.12
def main():
  n = int(input("Entre com o número: "))

  n_digits(n)


def n_digits(n):
  count = 0
  while(n >= 1):
    count = count+1
    n = n/10

  result = "O número dado tem "+str(count)+" digitos."

  print(result)


if __name__ == "__main__":
  main()
