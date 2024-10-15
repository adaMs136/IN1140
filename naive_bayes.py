
# 1. anntagelser: ord veies likt (naive), syntaks er irrelevant, tar ikke hensyn til pragmatikk


# 2.
# importerer en metode for å regne produktet av en liste med tall
from numpy import prod

# definerer en funksjon som tar inn en liste med ord og lager en ordbok med ordene og deres frekvens
def lag_ordbok(liste):
    ordbok = dict()
    for setning in liste:
        delt_setning = setning.split()
        for ord in delt_setning:
            if ord in ordbok:
                ordbok[ord] += 1
            else:
                ordbok[ord] = 1
    return ordbok

# definerer en funksjon som tar inn to ordbøker og teller antall unike ord i dem totalt
# dette blir lengden på vokabularet til treningsdataen
def ant_ordtyper(ordbok1, ordbok2):
    alle_ordtyper = list()
    for n in ordbok1:
        alle_ordtyper.append(n)
    for m in ordbok2:
        alle_ordtyper.append(m)

    return len(set(alle_ordtyper))


# funksjonen kjører en naiave bayes klassifisering av en setning gitt en nøstet liste med setninger fra hver klasse
def naive_bayes(setning, pos_setninger, neg_setninger):

    # lager ordbøkene med ord og deres frekvenser for begge klassene
    pos_ordbok = lag_ordbok(pos_setninger)
    neg_ordbok = lag_ordbok(neg_setninger)

    # finner totale antall setninger i treningsdataen
    ant_setninger = len(pos_setninger) + len(neg_setninger) # 7 setninger

    # gjør om setningen som skal klassifiseres til en liste med alle ordene
    ord_i_setning = setning.split()

    #teller hvor mange ord som finnes i hver av klassene
    tot_pos_ord = sum(pos_ordbok.values()) # 17 ord
    tot_neg_ord = sum(neg_ordbok.values()) # 20 ord

    #finner lengden på vokabularet for treningsdataen
    v = ant_ordtyper(pos_ordbok, neg_ordbok) # 30 ordtyper
    
    #lager tommer lister for sannsynlighetene til at et ord tilhører klassen
    pos_sans = []
    neg_sans = []

    # for hvert ord i setningen regnes ut sannsynligheten for at den tilhører en gitt klasse
    # sannsynligheten legges inn i listen med sannsynligheter for den klassen
    # detter er utregningen av P(w|c), hvor P(w|c) = antall forekomster av ordet i klasse c / antall ord i klassen
    # det brukes 'legg til én-glatting' så utttrykker blir: 
    # P(w|c) = (antall forekomster av ordet i klasse c + 1) / (antall ord i klassen + antall ordtyper i treningsdataen)
    for ordet in ord_i_setning:
        if ordet in pos_ordbok:
            pos_sans.append((pos_ordbok[ordet]+1)/(tot_pos_ord+v))

        else:
            pos_sans.append(1/(tot_pos_ord+v))
        
        if ordet in neg_ordbok:
            neg_sans.append((neg_ordbok[ordet]+1)/(tot_neg_ord+v))
        else:
            neg_sans.append(1/(tot_neg_ord+v))

    # regner ut den totale sannsynligheten for at setingen tilhører en klasse
    # dette er det samme som P(w|c) * P(c),
    # hvor P(c) = antall setninger gitt klasse * antall setninger totalt i treningsdataen
    tot_pos_sans = prod(pos_sans)*(len(pos_setninger)/ant_setninger)
    tot_neg_sans = prod(neg_sans)*(len(neg_setninger)/ant_setninger)

    #sammenligner den totale sannsynligheten for hver av klassene for å klassifisere setningen
    if tot_pos_sans == tot_neg_sans:
        return "?"
    elif tot_pos_sans > tot_neg_sans:
        return "POSITIV"
    else:
        return "NEGATIV"

# definerer et hovedprogram med kjørekoden
def hovedprogram():

    # legger inn setningene for den positive klassen og lager en nøstet liste med dem
    pos1 = "en fortreffelig start på konserten"
    pos2 = "et samspill og førsteklasses orkester"
    pos3 = "har aldri laget et ordentlig dårlig album"
    pos = [pos1, pos2, pos3]

    # legger inn setningene for den negative klassen og lager en nøstet liste med dem
    neg1 = "konserten viste seg å være én av de dårligste i mitt liv"
    neg2 = "oppskrytt orkester"
    neg3 = "kjedelig konsert"
    neg4 = "et ordentlig dårlig album"
    neg = [neg1, neg2, neg3, neg4]

    # skriver inn setningene som skal klassifiseres
    setning1 = "førsteklasses artist men dårlig og kjedelig album"
    setning2 = "fortreffelig orkester og flott album"

    # kjører naive bayes klassifiseringen og skriver ut resultatene i terminalen
    print(f"Setning nr 1 er {naive_bayes(setning1, pos, neg)}") # ble positiv
    print(f"Setning nr 2 er {naive_bayes(setning2, pos, neg)}") # ble positiv

#kjører hovedprogrammet
hovedprogram()


# 3.
# Jeg er enig med klassifiseringen av setning nr. 2, men ikke med setning nr. 1.
# Den sier "førsteklasses artist" som er positivt, men resten er negativt og det virker som annmeldelsen
# er ment for å være om albummet som beskrives på en negativ måte.

# For å få et mer riktig resultat kunne treningsdataen vært mer balansert (det var flere setninger
# og ord i den negative klassen).

# Det største problemet med treningsdataen vi hadde her var at mange av ordene i seg selv hadde motsatt
# konotasjon den den klassen de tilhørte. Denne er vanskelig å få fikset ettersom en maskin har vanskeligheter
# for å skille på pragmatikk, men et større korpus hadde nok hjulpet dette litt.