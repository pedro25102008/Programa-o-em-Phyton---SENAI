loja = {
'fone':100.00,
'livro':50.00,
'tablet':500.00
}

prod1 = input("digite o produo")
prod2 = input("digite o produo")
prod3 = input("digite o produo")
prod4 = input("digite o produo")

lista_prod = []
lista_valores = []

lista_prod.extend([prod1,prod2,prod3,prod4])
lista_valores +=(loja[prod1], loja[prod2], loja[prod3], loja[prod4])

soma = sum(lista_valores)
print('Produtos:', lista_prod)
print('...'*2)
print('R$', soma)






