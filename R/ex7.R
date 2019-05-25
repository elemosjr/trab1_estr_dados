#!/bin/Rscript

## Exercício 2.12
main <- function()
{
  cat("Entre com o número: ")
  n <- as.numeric(readLines("stdin", n = 1))
  
  count <- 0
  while(n >= 1)
  {
    count <- count+1
    n <- n/10
  }
  
  result <- paste("O número dado tem", count, "digitos.")
  
  return(result)
}

main()