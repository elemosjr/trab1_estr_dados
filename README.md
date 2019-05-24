
<!-- README.md foi gerado por README.Rmd -->

# Trabalho Estrutura de Dados

Primeiro trabalho da matéria estrutura de dados do curso de
Estatística-UEM.

# Primeira Metade

## 1.6

Escreva um programa para contar dinheiro que pergunte, dentro de um
monte de dinheiro, qual a quantidade de notas de:

  - 1 real;
  - 2 reais;
  - 5 reais;
  - 10 reais;
  - 50 reais;
  - 100 reais.

Em seguida programa imprime qual o valor total em dinheiro.

Exemplo: 2 notas de 1 real e 5 notas de 100 reais (entrada) dão um total
de 502 reais (saída).

## 1.7 Exercício

Escreva um programa que faça o inverso da questão anterior, ou seja,
solicite ao usuário um valor (total) em dinheiro, e informe quantas
notas de: 1 real, 2 reais, 5 reais, 10 reais, 50 reais e 100 reais serão
necessárias para compor este valor, de forma que seja utilizado o menor
número de notas possível.

Exemplo: 507 reais são 5 notas de 100 reais, 1 nota de 5 reais e 2 notas
de 1 real.

Bonus: minimize a quantidade de notas. No exemplo anterior poderia-se
usar 1 nota de 2 reais ao invés de 2 notas de 1 real.

## 1.8 Exercício

Uma agencia de espionagem encomendou um programa especial para fazer a
codificação de mensagens. O programa inicialmente lê a mensagem e
codifica da seguinte forma:

Considerando os caracteres que compõem a mensagem aos pares, cada
caractere é trocado com o seu vizinho, sempre levando em consideração
que isto é feito aos pares,como mostra o exemplo abaixo:

mensagem original: ‘Esta é uma mensagem.’;

processo codificação: ‘E s t a \_ é \_ u m a \_ m e n s a g e m .’;
(caracteres \_ indicam os espaços em branco)

mensagem codificada: ‘sEaté u amm neaseg.m’;

Se o número de caracteres for ímpar, o programa acrescenta um caractere
‘\#’ no final antes de realizar a troca dos pares.

## 2.7

  - Faça um programa que receba o valor de uma dívida e mostre uma
    tabela com os seguintes dados:
  - valor da dívida
  - valor dos juros
  - quantidade de parcelas
  - valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

| Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida |
| :--------------------: | :----------------------------------------: |
|           1            |                     0                      |
|           3            |                     10                     |
|           6            |                     15                     |
|           9            |                     20                     |
|           12           |                     25                     |

Exemplo de saída do programa:

| Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela |
| :-------------: | :-------------: | :--------------------: | :--------------: |
|   R$ 1.000,00   |        0        |           1            |   R$ 1.000,00    |
|   R$ 1.100,00   |       100       |           3            |    R$ 366,00     |
|   R$ 1.150,00   |       150       |           6            |    R$ 191,67     |

## 2.9

Faça um programa para imprimir:

1 1 2 1 2 3 ….. 1 2 3 … n

Para um n informado pelo usuário. Use uma função que receba um valor n
inteiro e imprima até a n-ésima linha.

## 2.11

Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -\> 721.

## 2.12

Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.

## 3.3

Faça uma função recursiva para retornar a soma dos digitos de um dado
número:

``` python
sum_digits(345) = 12 sum_digits(45) = 9
```

Caso queira, faça a versão iterativa primeiro.

# Segunda Metade

## Lista duplamente ligada

Implementar operações de lista duplamente ligadas:

Inserir (início, fim), remover, alterar, buscar e um método de
“print\_()”

  - Inserir não precisa retornar nada;
  - Remover retorna True ou False;
  - Alterar retorna True ou False;
  - Buscar retorna posição ou False.
