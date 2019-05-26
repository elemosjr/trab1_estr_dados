#!/bin/Rscript

## Exercicio 1.8 ed
main <- function()
{
  cat("Qual o valor? ")
  valor <- as.numeric(readLines("stdin", n = 1))

  notas_valor(valor)
}

notas_valor <- function(valor)
{
  resto <- valor
  quant <- c()
  nota <- c(1, 2, 5, 10, 50, 100)
  
  for(i in sort(nota, decreasing = TRUE))
  {
    quant <- c(quant, floor(resto/i))
    
    resto <- valor%%i
    
    if(resto == 0)
    {
      break()
    }
  }
  
  quant <- c(quant, rep(0, 6-length(quant)))
  
  quant <- rev(quant)
  
  text_nota <- ""
  
  for(i in 1:length(nota))
  {
    if(quant[i] == 0)
    {} else if(quant[i] == 1)
    {
      text_nota <- paste0(text_nota,
                          ", ",
                          quant[i], 
                          " nota de ", 
                          nota[i])
    } else
    {
      text_nota <- paste0(text_nota,
                          ", ", 
                          quant[i], 
                          " notas de ", 
                          nota[i])
    }
    
    if(quant[i] == 0)
    {} else if(nota[i] == 1)
    {
      paste0(text_nota, "real")
    } else
    {
      paste0(text_nota, "reais")
    }
  }
  
  text_nota <- gsub("^,\ ", "", text_nota)
  
  result <- paste0("A menor combinação possível de notas para dar o valor ", 
         valor, 
         " é ", 
         text_nota)
      
  return(result)
}

main()
