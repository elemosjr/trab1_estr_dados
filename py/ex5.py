#!/bin/python

## Exercício 2.9
def main():
  n = int(input("Informe um n: "))

  seq_n(n)


def seq_n(n):
  lista = []

  for i in range(1, n+2):
    lista = [f' {x} '.format(x) for x in map(str, list(range(1,i)))]
    print("".join(lista))


if __name__ == "__main__":
  main()
