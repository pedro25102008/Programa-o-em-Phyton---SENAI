nome= input("nome do aluno")

nota1 =float (input("nota1"))
nota2 =float (input("nota2"))
nota3 =float (input("nota3"))
nota4 =float (input("nota4"))
nota5 =float (input("nota5"))

média = (nota1+nota2+nota3+nota4+nota5)/5
print( 'média do aluno:',nome, '=', média)

requisito1 = média >= 7
requisito2 = média >= 5 and média <=6.9
requisito3 = média < 5

print(f'''
situação do aluno {nome}
APROVADO = {requisito1}
RECUPERAÇÃO = {requisito2}
REPROVADO = {requisito3}
''')
