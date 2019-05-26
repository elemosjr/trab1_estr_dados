#!/bin/Rscript

## Exercício 1.8
main <- function()
{
  cat("Entre com o texto para a codificação: ")
  string <- as.character(readLines("stdin", n = 1))

  codificar(string)
}

codificar <- function(string)
{
  lista <- strsplit(string, "")[[1]]

  if(length(lista)%%2 == 1)
  {
    n <- length(lista)+1
    lista <- c(lista, "#")
  } else
  {
    n <- length(lista)
  }

  lista_n <- c()
  
  for(i in 1:n)
  {
    if(i%%2 == 0)
    {
      lista_n <- c(lista_n, i)
    }
  }
  
  text <- ""
  
  for(i in lista_n)
  {
    text <- paste0(text,
                   as.character(lista[i]),
                   as.character(lista[i-1]))
  }
  
  return(text)
}

main()
