import random
import math
import numpy as np 
import matplotlib.pyplot as plt



def verjetnost_najboljsi_kandidat(n,r):
    k = (r-1) / n
    vsota = 0
    for i in range(r,n+1):
        vsota += 1/(i-1)
    return (k * vsota)

def tabela_partnerjev(n, m):
    # n... število kandidatk
    # m... kolikokrat poženemo proces iskanja najbolšega partnerja
    tabela_partnerjev = {}
    for i in range(m):
        partnerji = list(range(1, n+1))
        random.shuffle(partnerji)
        tabela_partnerjev[i] = partnerji

    return tabela_partnerjev

def narisi_graf(i, vsotke, m):
    # i - Število potencialnih partnerjev
    ver_i = []
    for stop in range(i):
        ver_i.append(vsotke[(i,stop)] / m) 

    x = [j/i for j in range(i)]

    plt.plot(x, ver_i)
    plt.show()


def NajbolsiPartner(partnerji, stop):
    """Funkcija, ki vrne izbranega partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 

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
   
    return za_vedno


def NajbolsiPartner_povprecje(partnerji, stop, alfa):
    """Funkcija, ki vrne izbranega partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 
    # alpha ... faktor s katerim pomnožimo povprečje

    vzorec = partnerji[:stop] #vključno s stop
    dovolj_dober = np.mean(vzorec) * alfa

    poroka = partnerji[stop:]
    za_vedno = 0
    
    for partner in poroka:
        if (partner >= dovolj_dober):
            za_vedno = partner
            break
   
    return za_vedno

def NajbolsiPartner_enako(partnerji, stop):
    """Funkcija, ki vrne izbranega partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 

    vzorec = partnerji[:stop] #vključno s stop
    poroka = partnerji[stop:]

    najbolši = 0 
    za_vedno = 0
    for partner in vzorec:
        if (partner > najbolši):
            najbolši = partner
   
    for partner in poroka:
        if (partner >= najbolši): #Spremenimo, da je tudi enako vredu
            za_vedno = partner
            break
   
    return za_vedno


def NajbolsiPartner_zadnji(partnerji, stop):
    """Funkcija, ki vrne izbranega partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja. 
    Ob primeru, da smo bili pri iskanju partnerja neuspešni pa se poročimo z zadnjim kandidatom."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 

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
   
    if za_vedno == 0:
        za_vedno = poroka[-1]

    return za_vedno


def NajbolsiPartner_povprecje_zadnji(partnerji, stop, alfa):
    """Funkcija, ki vrne izbranega partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 
    # alpha ... faktor s katerim pomnožimo povprečje

    vzorec = partnerji[:stop] #vključno s stop
    dovolj_dober = np.mean(vzorec) * alfa

    poroka = partnerji[stop:]
    za_vedno = 0
    
    for partner in poroka:
        if (partner >= dovolj_dober):
            za_vedno = partner
            break

    if za_vedno == 0:
        za_vedno = poroka[-1]
   
    return za_vedno


def NajbolsaDvaPartnerja(partnerji, stop):
    """Funkcija, ki vrne izbrana partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja. 
    Nato pa izbrali naslednja dva, ki sta bila boljša od vseh, ki smo jih videli v vzorcu."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 

    vzorec = partnerji[:stop] #vključno s stop
    poroka = partnerji[stop:]

    najbolši = 0 
    za_vedno = []

    for partner in vzorec:
        if (partner > najbolši):
            najbolši = partner
   
    for partner in poroka:
        if (partner > najbolši):
            za_vedno.append(partner)
        if len(za_vedno) == 2:
            break 
   
    return za_vedno


def NajbolsaDvaPartnerja_povprecje(partnerji, stop, alfa):
    """Funkcija, ki vrne izbrana partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 
    # alpha ... faktor s katerim pomnožimo povprečje

    vzorec = partnerji[:stop] #vključno s stop
    dovolj_dober = np.mean(vzorec) * alfa

    poroka = partnerji[stop:]
    za_vedno = []
    
    for partner in poroka:
        if (partner >= dovolj_dober):
            za_vedno.append(partner)
            if len(za_vedno) == 2:
                break 

    return za_vedno


def Najbolsih_k_partnerjev(partnerji, stop, k):
    """Funkcija, ki vrne izbrana partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja. 
    Nato pa izbrali naslednja dva, ki sta bila boljša od vseh, ki smo jih videli v vzorcu."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 
    # k ... število partnerjev, ki jih želimo izbrati

    vzorec = partnerji[:stop] #vključno s stop
    poroka = partnerji[stop:]

    najbolši = 0 
    za_vedno = []

    for partner in vzorec:
        if (partner > najbolši):
            najbolši = partner
   
    for partner in poroka:
        if (partner > najbolši):
            za_vedno.append(partner)
        if len(za_vedno) == k:
            break 

    if za_vedno == []:
        za_vedno.append(0)
   
    return za_vedno




def Najbolsih_k_partnerjev_povprecje(partnerji, stop, alfa, k):
    """Funkcija, ki vrne izbrana partnerja izmed partnerjev, 
    če smo smo jih zavračali do stop partnerja."""
    # partnerji ... seznam partnerjev
    # stop ... kdaj nehamo zavračati vse partnerje 
    # alpha ... faktor s katerim pomnožimo povprečje

    vzorec = partnerji[:stop] #vključno s stop
    dovolj_dober = np.mean(vzorec) * alfa

    poroka = partnerji[stop:]
    za_vedno = []
    
    for partner in poroka:
        if (partner >= dovolj_dober):
            za_vedno.append(partner)
            if len(za_vedno) == k:
                break 

    if za_vedno == []:
        za_vedno.append(0)

    return za_vedno





def bonus(partnerji, stop):

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
    
    if za_vedno == 0:
        za_vedno = random.randint(0,1) * max(partnerji)
   
    return za_vedno


def bonus2(partnerji, stop,p):

    vzorec = partnerji[:stop] #vključno s stop
    poroka = partnerji[stop:]

    najbolši = 0 
    za_vedno = 0

    for partner in vzorec:
        if (partner > najbolši):
            najbolši = partner
   
    for partner in poroka:
        if (partner > najbolši) and (random.random() > p):
            za_vedno = partner
            break
    
    if za_vedno == 0:
        za_vedno = random.randint(0,1) * max(partnerji)
   
    return za_vedno











