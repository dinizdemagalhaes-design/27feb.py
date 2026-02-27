Fofo = float(input("preco do primeiro amaciante 1"))
Downy = float(input( "preco do segundo amaciante 2"))

if Fofo<Downy:
    diferenca = Downy - Fofo
    print("o Fofo e mais barato")
elif Downy<Fofo:
    diferenca = Fofo - Downy
    print("o Downy e mais barato")
else:
    print("Os dois tem o mesmo preco")
