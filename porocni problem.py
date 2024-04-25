import random
import math



def printNajbolšiPartner(n, stop):
    """Funkcija, ki vrne izbranega partnerja izmed n partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # n ... št. potencialnih partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 

    #zgeneriramo naš vzorec
    # predpostavimo, da ne morata biti dva kandidata enako dobra
    partnerji = list(range(1,n+1))
    random.shuffle(partnerji)
    # print(partnerji)

    vzorec = partnerji[:stop] #vključno s stop
    poroka = partnerji[stop:]


    najbolši = 0 
    za_vedno = 0
    for partner in vzorec:
        if (partner > najbolši):
            najbolši = partner
   
    for partner in poroka:
        if (partner > najbolši):
            za_vedno = partner
            break
   

    # if (za_vedno):
    #     print("\nPoročim se s partnerjem", za_vedno)
    # else:
    #     print("\nNisem našel partnerja.")
   
    return za_vedno





# Preverimo, kako uspešni smo, če se držimo pravila 1/e = 0.36787944
n = 1000 #kolikokrat poženemo proces iskanja najbolšega partnerja
m = 100 # število vseh kandiatov  


vsota = 0 
for i in range(n):
    if printNajbolšiPartner(m, round(m * 0.36787944)) == m :
        vsota += 1


print(vsota/n)












# Matrika vsotke - procenti, da bomo uspešni za različni stop
n = 10000 #kolikokrat poženemo proces iskanja najbolšega partnerja
m = 20 # število vseh kandiatov  


vsotke = [0] * m
for stop in range(m-1):
    for _ in range(n):
        if printNajbolšiPartner(m, stop) == m :
            vsotke[stop] += 1

print(vsotke)





