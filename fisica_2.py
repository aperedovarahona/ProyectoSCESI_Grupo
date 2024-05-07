print("Movimiento Rectilineo Uniformemente Variado (Ecuacion sin aceleracion)")
print("M.R.U.V.","D=((Vo+Vf)/2)T <- FORMULA")
print("¿Cúal es el valor qué deseas hallar")
print("1=Distancia") 
print("2=Velocidad inicial")
print("3=Velocidad final") 
print("4=Tiempo")
m=input()
j=int(m)
if j==1:
    print("Prara hallar la DISTANCIA ingrese:")
    o=int(input("La velocidad inicial"))
    f=int(input("La velocidad final"))
    t=int(input("El tiempo"))
    d=((o+f)/2)*t
    print("La distancia es",d,"metros")

elif j==2:
    print("Prara hallar la VELOCIDAD INICIAL ingrese:")
    d=int(input("La distancia"))
    f=int(input("La velocidad final"))
    t=int(input("El tiempo"))
    o=((2*d)/t)-f
    print("La velocidad inicial es",o,"metros por segundo")

elif j==3:
    print("Prara hallar la VELOCIDAD FINAL ingrese:")
    d=int(input("La distancia"))
    o=int(input("La velocidad inicial"))
    t=int(input("El tiempo"))
    f=((2*d)/t)-o
    print("La velocidad final es",f,"metros por segundo")

elif j==4:
    print("Prara hallar el TIEMPO ingrese:")
    o=int(input("La velocidad inicial"))
    f=int(input("La velocidad final"))
    d=int(input("La distancia"))
    t=(d*2)/(o+f)
    print("El tiempo es",t,"segundos")
else:
    print("Opcion invalida")