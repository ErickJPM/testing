def orden_ascendente(arreglo):
    return sorted(arreglo)

def personas_mayores(arregloDiccionarios):
    contador=0
    for personas in arregloDiccionarios:
        if(personas['edad']>18):
            contador+=1
    return contador
