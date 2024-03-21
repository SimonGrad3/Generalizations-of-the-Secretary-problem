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
    print(partnerji)

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
   

    if (za_vedno):
        print("\nPoročim se s partnerjem", za_vedno)
    else:
        print("\nNisem našel partnerja.")
   




#100 partnerjev prvih 37 zavrnem    
printNajbolšiPartner(100, 37)



