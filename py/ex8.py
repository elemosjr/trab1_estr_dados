#!/bin/python

## Exercício 3.3
def main():
  n = str(input("Entre com o número: "))

  print(sum_digits(n))


def sum_digits(n):
  lista = list(map(int, list(n)))
  new_n = "".join(list(map(str, lista[1:])))
  res_n = lista[0]

  if new_n != '':
    res_n = res_n + sum_digits(new_n)
  else:
    return(res_n)

  return(res_n)


if __name__ == "__main__":
  main()
