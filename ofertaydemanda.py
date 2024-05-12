def oferta(precio, coeficientes):
    return coeficientes[0] + coeficientes[1] * precio

def demanda(precio, coeficientes):
    return coeficientes[0] - coeficientes[1] * precio

def precio_equilibrio(oferta_coeficientes, demanda_coeficientes):
    for precio in range(100):  # Suponemos que el precio no superará 100
        if oferta(precio, oferta_coeficientes) == demanda(precio, demanda_coeficientes):
            return precio
    return None  

def cantidad_equilibrio(precio, demanda_coeficientes):
    if precio is not None:
        return demanda(precio, demanda_coeficientes)
    else:
        return None


print("Ingrese los coeficientes para la función de oferta:")
constante_oferta = int(input("Ingrese el coeficiente constante: "))
coeficiente_precio_oferta = int(input("Ingrese el coeficiente de la variable de precio: "))
oferta_coeficientes = [constante_oferta, coeficiente_precio_oferta]

print("Ingrese los coeficientes para la función de demanda:")
constante_demanda = int(input("Ingrese el coeficiente constante: "))
coeficiente_precio_demanda = int(input("Ingrese el coeficiente de la variable de precio: "))
demanda_coeficientes = [constante_demanda, coeficiente_precio_demanda]


precio_eq = precio_equilibrio(oferta_coeficientes, demanda_coeficientes)


cantidad_eq = cantidad_equilibrio(precio_eq, demanda_coeficientes)


if precio_eq is not None and cantidad_eq is not None:
    print("El precio de equilibrio es:", precio_eq)
    print("La cantidad de equilibrio es:", cantidad_eq)
else:
    print("No se encontró un precio de equilibrio en el rango proporcionado.")
