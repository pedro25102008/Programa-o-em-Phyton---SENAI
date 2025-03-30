nome = input ("Olá, digite seu nome")
print (f'Olá, {nome}, seja bem vindo!')


numero1 = float (input (f'digite um número para a multiplicação , {nome}'))
numero2 = float (input (f'digite outro que deseja multitiplicar'))
resultado1 = numero1*numero2
print ("o resultado da sua multiplicação é", resultado1)

numero3 = int (input (f'agora, digite um número para a divisão , {nome}'))
numero4 = int (input (f'digite outro que deseja dividir'))
resultado2 = numero3/numero4
print ("o resultado da sua divisão é", resultado2)

numero5 = int (input (f'agora, digite um número para a subtração , {nome}'))
numero6 = int (input (f'digite outro que deseja subtrair'))
resultado3 = numero5-numero6
print ("o resultado da sua divisão é", resultado3)

numero7 = float (input (f'agora, vamos para uma multiplicação de 4 números, digite o primeiro'))
numero8 = float (input (f'digite outro para a multiplicação'))
numero9 = float (input (f'digite mais um'))
numero10 = float (input (f'digite o último númnero'))
resultado4 = numero7*numero8*numero9*numero10
print ("o resultado da sua soma é", resultado4)

numero_dobro = float (input (f'agora, digite um número para vermos seu dobro'))
print (f' o dobro do número {numero_dobro} é {numero_dobro*2}')
