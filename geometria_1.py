print ("Teorema de Pitagoras")
name=input ("ingrese su nombre")
print (name,"¿qué funcion deseas hallar?")
print( "1=cateto adyacente, 2=cateto opuesto, 3=hipotenusa")
m=input()
j=int(m)
if j==3:
    print ("para hallar hipotenusa ingrese")
    x=int(input("ingrese cateto adyacente"))
    y=int(input("ingrese cateto opuesto"))
    z=(x**2+y**2)**0.5
    print (z)
if j==1:
    print ("para hallar cateto adyacente ingrese")
    z=int(input("ingrese hipotenusa"))
    y=int(input("ingrese cateto opuesto"))
    x=(z**2-y**2)**0.5
    print (x)   
if j==2:
    print ("para hallar cateto opuesto ingrese")
    z=int(input("ingrese hipotenusa"))
    x=int(input("ingrese cateto adyacente"))
    y=(z**2-x**2)**0.5
    print (y)
