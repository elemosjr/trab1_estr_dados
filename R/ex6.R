#!/bin/Rscript

## Exercício 2.11
main <- function()
{
  cat("Entre com o número: ")
  n <- readLines("stdin", n = 1)

  string <- strsplit(as.character(n),"")[[1]]
  
  string <- string[length(string):1]
  
  result <- paste(as.character(n), "->", paste(string, collapse = ""))
  
  return(result)
}

main()