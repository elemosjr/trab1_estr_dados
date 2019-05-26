#!/bin/python

def main():
  string = str(input("Entre com o texto para codificação: "))
  codificar(string)

  
def codificar(string):
  lista = list(string)
  
  if len(lista)%2 == 1:
    n = len(lista)+1
    lista.append("#")
  else:
    n = len(lista)
  
  lista_n = []
    
  for i in range(1, n+1):
    if i%2 == 1:
      lista_n.append(i)
      
  text = ""
    
  for i in lista_n:
    text = text+str(lista[i])+str(lista[i-1])
  
  print(text)
  
if __name__ == "__main__":
  main()
