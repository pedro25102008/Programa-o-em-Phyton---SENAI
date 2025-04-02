import random



numero = int (input("digite seu numero"))
def jogo (numero) :
    if numero % 2 == 0 :
        print ("seu numero é par")
    if numero % 2 == 1 :
        print ("seu numero é impar")

jogo(numero)



#CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.



numero1 = int(input("digite o primeiro numero para multiplicar"))
numero2 = int(input("digite o segundo numero para a multiplicação"))
numero3 = int(input("digite o terceiro e ultimo numero para multiplicar"))

def mul() :
  mul = (numero1*numero2*numero3)
  print(mul)

mul ()
