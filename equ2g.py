import math
print("ANNA AN i ONA VILÀ, 2n ESO B")
print("Benvinguts al programa de resolució d'equacions de 2n grau")
print("tipus ax2 + bx + c = 0")

textA = input("ENTRA a ")
textB = input("ENTRA b ")
textC = input("ENTRA c ")

print("El valor de a és:", textA)
print("El valor de b és:", textB)
print("El valor de c és:", textC)

valA = int(textA)
valB = int(textB)
valC = int(textC)

print("Valor entrats correctes, molt bé!")

valDiscriminant = valB * valB - 4 * valA * valC

print("El valor del discriminant és:", valDiscriminant)

if valDiscriminant < 0 :
    print("Aquesta equació malauradament no té solució")
else :
    valArrelDisc = math.sqrt(valDiscriminant)
    print(valArrelDisc)
    x1 = (-valB + valArrelDisc) / (2 * valA)
    print("Ja tenim la solució d'aquesta equació de 2n grau!!")
    if valDiscriminant == 0 :
        print(x1)
    else:
        x2 = (-valB - valArrelDisc) / (2 * valA)
        print(x1, x2)
     
