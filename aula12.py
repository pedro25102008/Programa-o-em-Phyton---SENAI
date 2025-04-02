import random


#CRIE 3 NUMEROS ALEATORIOS
numero_aleatorio = random.randint (1,3)
print (numero_aleatorio)


#Crie um número aleatório entre 10 a 30 utilize o range()
numero_aleatori = random.randrange (10,30)
print (numero_aleatori)


#Contagem regressiva simples*
#Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
def contagem () :
    numero10 = (10)
    numero9 = (9)
    numero8 = (8)
    numero7 = (7)
    numero6 = (6)
    numero5 = (5)
    numero4 = (4)
    numero3 = (3)
    numero2 = (2)
    numero = (1)


contagem ()
print (contagem)

#Soma de números pares*
#Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
#(use módulo, if, for)




#Tabuada de multiplicação*
#Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
#(while ou for )
tab = int(input("digite um numero intero e mostraremos sua tabuada"))
lista_mult = []
mult = (tab * 1)
mult2 = (tab * 2)
mult3 = (tab * 3)
mult4 = (tab * 4)
mult5 = (tab * 5)
mult6 = (tab * 6)
mult7 = (tab * 7)
mult8 = (tab * 8)
mult9 = (tab * 9)
mult10 = (tab * 10)
lista_mult.append (mult)
lista_mult.append (mult2)
lista_mult.append (mult3)
lista_mult.append (mult4)
lista_mult.append (mult5)
lista_mult.append (mult6)
lista_mult.append (mult7)
lista_mult.append (mult8)
lista_mult.append (mult9)
lista_mult.append (mult10)
print (lista_mult)

#Números ímpares reversos
#Exiba uma contagem regressiva de números ímpares de 99 a 1.