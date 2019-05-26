#!/bin/python

## Exercício 2.11
def main():
  n = str(input("Entre com o número: "))

  rev_number(n)

def rev_number(n):
  string = list(n)

  string.reverse()

  result = n+" -> "+"".join(string)

  print(result)


if __name__ == "__main__":
  main()
