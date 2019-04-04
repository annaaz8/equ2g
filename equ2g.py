import math

print("benvingudes al programa de resolucio d'equacions de 2n grau")
print("tipus ax2 + bx + c = 0")

textA = input("ENTRA a ")
textB = input("ENTRA b ")
textC = input("ENTRA c ")

print("el valor de a es:", textA)
print("el valor de b es:", textB)
print("el valor de c es:", textC)

valA = int(textA)
valB = int(textB)
valC = int(textC)

print("valor entrats correctes, molt be!")

print("el valor de a es:", valA)
print("el valor de b es:", valB)
print("el valor de c es:", valC)

valDiscriminant = valB * valB - 4 * valA * valC

print("el valor del discriminant es:", valDiscriminant)

if valDiscriminant < 0 :
    print("aquesta equacio malauradament no te solucio")
else :
    print("seguim")
    valArrelDisc = math.sqrt(valDiscriminant)
    print(valArrelDisc)
    x1 = (-valB + valArrelDisc)/ (2 * valA)
    x2 = (-valB - valArrelDisc)/ (2 * valA)
    print("ja tenim la solució d'aquesta equacio de 2n grau!!!!")
    print(x1, x2)
