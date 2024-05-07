print("M.R.U.")
print("¿Qué valor deseas hallar")
print("1=distancia[m.], 2=tiempo[s.], 3=velocidad[m./s.]")
m=input()
j=int(m)
if j==1:
    print("Para hallar la DISTANCIA ingrese:")
    v=int(input("ingrese la velocidad en metros sobre sengundos]"))
    t=int(input("ingrese el tiempo [en segundos]"))
    d=v*t
    print("La distancia es",d,"metros")
if j==2:
    print("Para hallar la VELOCIDAD ingrese:")
    d=int(input("ingrese la distancia [en metros]"))
    t=int(input("ingrese el tiempo [en segundos]"))
    v=d/t
    print("La velocidad es",v,"metros sobre segundo")
if j==3:
    print("Para hallar el TIEMPO ingrese:")
    v=int(input("ingrese la velocidad [en metros sobre sengundos]"))
    d=int(input("ingrese la distancia [en metros]"))
    t=v*t
    print("El tiempo es",t,"segundos")
