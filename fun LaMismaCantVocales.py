#  Hacer un programa que solicite el ingreso de 2 palabras que deben ser distintas y determine si ambas tienen la misma cantidad de vocales
# (aunque estas sean distintas).

def LaMismaCantVocales(cad1,cad2):
    cont1=0
    cont2=0
    for i in range(len(cad1)):
        if EsVocal(lista[i]):
            cont1=cont1+1
    for j in range(len(cad2)):
        if EsVocal(lista[j]):
            cont2=cont2+1
    if cont1==cont2:
        return(cont1)
    else:
        return(false)
