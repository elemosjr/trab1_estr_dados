#!/bin/Rscript

## Exercício 2.7
main <- function()
{
  cat("Qual o valor? ")
  valor <- as.numeric(readLines("stdin", n = 1))
  
  juros(valor)
}

juros <- function(valor)
{
  total_juros <- c(valor,
                   valor*1.1,
                   valor*1.15,
                   valor*1.2,
                   valor*1.25)
  
  parcelas <- c(1,3,6,9,12)
  
  df <- data.frame(Valor_da_Divida = total_juros,
                   Valor_dos_Juros = total_juros - valor,
                   Quantidade_de_Parcelas = parcelas,
                   Valor_da_Parcela = total_juros / parcelas)
  
  return(df)
}

main()
