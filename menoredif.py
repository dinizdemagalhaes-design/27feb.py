Fofo = float(input("preco do primeiro amaciante 1"))
Downy = float(input( "preco do segundo amaciante 2"))


if Fofo<Downy:
    diferenca = Downy - Fofo
    mais_barato = Fofo
    diferenca = Downy -Fofo
elif Downy<Fofo:
    mais_barato = Downy
    diferenca = Fofo -Downy
else:
    mais_barto = Fofo
    diferenca = Fofo-Downy



print("preco mais barato")
print (diferenca)
    

