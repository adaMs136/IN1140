#importerer alle ressursene vi trenger
from nltk.corpus import brown
from random import randint


''' Universal Part-of-Speech Tagset (https://www.nltk.org/book/ch05.html#tab-universal-tagset): 
Tag     Meaning                 English Examples
ADJ	    adjective	            new, good, high, special, big, local
ADP	    adposition	            on, of, at, with, by, into, under
ADV	    adverb	                really, already, still, early, now
CONJ	conjunction	            and, or, but, if, while, although
DET	    determiner, article	    the, a, some, most, every, no, which
NOUN	noun	                year, home, costs, time, Africa
NUM	    numeral	                twenty-four, fourth, 1991, 14:24
PRT	    particle	            at, on, out, over per, that, up, with
PRON	pronoun	                he, their, her, its, my, I, us
VERB	verb	                is, say, told, given, playing, would
.	    punctuation marks	    . , ; !
X	    other                   ersatz, esprit, dunno, gr8, univeristy
'''

# henter ut alle ordene og deres tagger til en liste
# hvert ord er representert i listen som en tuple med ordet og ordklassen
# spesifiserer tagset for å få det spesifikke tagsettet vi ønsker (gitt over)
brown_ord = brown.tagged_words(categories="romance", tagset="universal") 

#lager en boolsk variabel for å fortsette while-løkken
fortsett = True
while fortsett:
    tilfeldig_index = randint(0, len(brown_ord)-1) # må ha -1 fordi randint(x, y) tar fra og med x, til og med y

    ordet = brown_ord[tilfeldig_index] # henter ut en tilfeldig tuple fra listen med alle ordene
    
    print(f"\nHvilken ordklasse tilhører '{ordet[0]}' ?")
    
    for i in range(2, -1, -1): 
    # range(x, y, z) tar fra og med x, til men ikke med y, med steg z. Derfor får vi at i blir 2, 1, 0 i iterasjonene av for-løkken
        klasse = input("> ")
        if klasse == ordet[1]:
            print("Riktig!")
            break # går ut av for-løkken ved riktig svar
        print(f"Det var feil... Du har {i} forsøk igjen")

    
    svar = input("\nTrykk 'enter' for å fortsette...")
    if svar != "":
        fortsett = False

print()