#!/bin/Rscript

## Exercício 3.3
main <- function()
{
  cat("Entre com o número: ")
  n <- as.numeric(readLines("stdin", n = 1))
  
  paste("A soma dos digitos de", n, "é", sum_digits(n))
}

sum_digits <- function(n)
{
  new_n <- as.numeric(
    paste(
      strsplit(
        as.character(n), "")[[1]][-1], 
          collapse = "")
  )

  res_n <- as.numeric(
    strsplit(
      as.character(n), "")[[1]][1]
  )

  if(!is.na(new_n))
  {
    res_n <- res_n + as.numeric(sum_digits(new_n))
  } else
  {
    return(res_n)
  }
  return(res_n)
}

main()
