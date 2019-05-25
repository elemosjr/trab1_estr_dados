#!/bin/Rscript

## Exercício 2.9
main <- function()
{
  cat("Informe um n: ")
  n <- as.numeric(readLines("stdin", n = 1))
  
  vetor <- c()
  
  for(i in 1:n)
  {
    vetor <- c(vetor, 1:i)
  }
  
  return(vetor)
}

main()