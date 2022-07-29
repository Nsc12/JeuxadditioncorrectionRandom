import random
from unittest import result


nb=1
score=0
while nb<=20:
    aleat1 = random.randint(1, 9)
    aleat2 = random.randint(1, 9)
    # Si exercice trop facile changez le nombre 9 !

    print("Combien fait", aleat1, "+" ,aleat2)
    reponse = int(input("Ta réponse = " ))
    nb = nb + 1
    result = (aleat1 + aleat2)
    if reponse == result:
        score = score + 1
    elif reponse != result:
        score = score +0
    print("Voici la correction", result)
print("Ton score est:", score, "/20")
if score >=16:
    print("Bravo")
if score <= 15:
    print("Bon")
if score<16 and score >=10:
    print("Dommage mais Ressaye")
