#!/bin/Rscript

## Exercício 2.12
main <- function()
{
  cat("Entre com o número: ")
  n <- as.numeric(readLines("stdin", n = 1))

  n_digits(n)
}

n_digits <- function(n)
{
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