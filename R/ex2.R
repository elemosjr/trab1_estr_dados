#!/bin/Rscript

## Exercicio 1.8 ed
main <- function(valor = 0)
{
  resto <- valor
  quant <- c()
  nota <- c(1, 2, 5, 10, 50, 100)
  
  for(nota in sort(nota, decreasing = TRUE))
  {
    quant <- c(quant, floor(resto/nota))
    
    resto <- valor%%nota
    
    if(resto == 0)
    {
      break()
    }
  }
  
  quant <- c(quant, rep(0, 6-length(quant)))
  
  return(quant)
}

main(as.integer(commandArgs(trailingOnly = 1)[1]))