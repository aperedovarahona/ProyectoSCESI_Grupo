print("Área de un cuadrilatero")
print("¿Qué valor deseas hallar")
print("1=Área, 2=Base, 3=Altura")
m=input()
j=int(m)
if j==1:
    print("Para hallar el ÁREA:")
    b=int(input("ingrese la base"))
    h=int(input("ingrese la altura"))
    a=b*h
    print("El area es",a,"unidades cuadradas")
if j==2:
    print("Para hallar la BASE:")
    a=int(input("ingrese el área"))
    h=int(input("ingrese la altura"))
    b=a/h
    print("La base es",v)
if j==3:
    print("Para hallar la ALTURA")
    a=int(input("ingrese el área"))
    b=int(input("ingrese la base"))
    h=a/b
    print("La altura es",h)
