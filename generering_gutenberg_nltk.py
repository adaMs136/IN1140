
#importerer alle nødvendige eksterne midler
from collections import defaultdict
from nltk.corpus import gutenberg
from nltk import bigrams
import numpy as np

#lagrer variabler for aspektene av teksten som trengs
bibel_tekst = "bible-kjv.txt"
bibel_ord = gutenberg.words(bibel_tekst)
bibel_setninger = gutenberg.sents(bibel_tekst)

#finner antall tokens
ant_tokens = len(bibel_ord)
print(f"Antall tokens: {ant_tokens}")

#finner antall ordtyper 
bibel_ordtyper = {ord.lower() for ord in bibel_ord}
ant_ordtyper = len(bibel_ordtyper)
print(f"Antall ordtyper: {ant_ordtyper}")


#lager tommer ordbøker for alle ulike bigrammer og bigrammodellen
unik_bigram_frekv = defaultdict(lambda: defaultdict(lambda: 0))
bigrammodell = defaultdict(lambda: defaultdict(lambda: 0.0))

#legger inn alle bigrammene i teksten med antall forekomster av dem 
for setning in bibel_setninger:
    for ord1, ord2 in bigrams(setning, pad_right=True, pad_left=True):
        unik_bigram_frekv[ord1][ord2] += 1

#lager en bigrammodell med sannsynlighet for hvert enkelt bigram
for foregående_ord in unik_bigram_frekv:
    telling_pr_ord = sum(unik_bigram_frekv[foregående_ord].values())
    for ord2 in unik_bigram_frekv[foregående_ord]:
        bigrammodell[foregående_ord][ord2] = unik_bigram_frekv[foregående_ord][ord2] / telling_pr_ord


#generering av tekst
#starter listen med teksten
tekst = [None]

#initsierer en løkke 
fortsett = True
while fortsett:
    forrige_ord = tekst[-1]
    
    #finner de mulige følgende ordene og deres respektive sannsynligheter
    mulige_ord = list(bigrammodell[forrige_ord].keys())
    sanns_ord = list(bigrammodell[forrige_ord].values())

    #henter ut det neste ordet og legger det til tekst-listen
    tekst.append(np.random.choice(mulige_ord, p=sanns_ord))
    lengde = len(tekst)

    #stopper løkken om det dukker opp en setningsslutt og det er 50 er flere ord i teksten
    if (tekst[-1] == None) and lengde >= 50:
        fortsett = False

#skriver ut tekst-listen
print()
print(tekst)

#henter sannsynlighetene for bigrammene i teksten og regner dem ut til den
#totale sannsynligheten for teksten
bigrammer_i_tekst = bigrams(tekst)
bigram_sannsynligheter = []
for bigram in bigrammer_i_tekst:
    bigram_sannsynligheter.append(bigrammodell[bigram[0]][bigram[1]])

sum_sanns = np.prod(bigram_sannsynligheter)
print(f"\nSannsynligheten for setningen er: {sum_sanns}")


#skriver ut teksten til en ny fil
fil = open("bibel_tekst.txt", "a")
fil.write("\n")
for ord_bibel in tekst:
    if ord_bibel == None:
        fil.write("\n")
    else:
        fil.write(ord_bibel+" ")
fil.close()