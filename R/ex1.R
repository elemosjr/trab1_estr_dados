#!/bin/Rscript

## Exercicio 1 ed
main <- function(notas = NULL)
{
  val_nota <- c(1,2,5,10,50,100)
  
  if(is.null(notas))
  {
    notas <- c()
    
    cat("Quantas notas de 1 real tem no monte? ")
    notas[1] <- as.integer(readLines("stdin", n = 1))
    
    for(i in 2:6)
    {
      cat(paste("Quantas notas de ",
                val_nota[i], 
                "reais tem no monte? "))
      notas[i] <- as.integer(
        readLines("stdin", n = 1))
    }
  }
  
  valor <- 0
  
  for(i in 1:6)
  {
    valor <- valor+(notas[i]*val_nota[i])
  }

  text_nota <- ""
  
  for(i in 1:6)
  {
    if(notas[i] == 0)
    {} else if(notas[i] == 1)
    {
      text_nota <- paste0(text_nota,
                         ", ",
                         notas[i], 
                         " nota de ", 
                         val_nota[i])
    } else
    {
      text_nota <- paste0(text_nota,
                          ", ", 
                          notas[i], 
                          " notas de ", 
                          val_nota[i])
    }
    
    if(notas[i] == 0)
    {} else if(val_nota[i] == 1)
    {
      paste0(text_nota, "real")
    } else
    {
      paste0(text_nota, "reais")
    }
  }
  
  text_nota <- gsub("^,\ ", "", text_nota)
  
  result <- paste0(text_nota, " dão um total de R$ ", valor, " reais.")

  return(result)
}

main()