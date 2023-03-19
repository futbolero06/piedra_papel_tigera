# programa para simular el lanzamiento de un dado

import random

print("------------------------------------------")
print("---------PIEDRA, PAPEL O TIGERA----------")
print("------------------------------------------")

# input 
jugador= int(input("escoje piedra(1),papel(2) o tigera(3): ",))
# processing

maquina = random.choice(["piedra","papel","tigera"])


if (maquina=="piedra"):
    if (jugador==1):
        rta="empate"
    elif (jugador==2):
        rta= "ganaste"
    else:
        rta="perdiste"

if (maquina=="papel"): 
    if (jugador==2):
        rta="empate"
    elif (jugador==3):
        rta= "ganaste"
    else:
        rta="perdiste"

if (maquina=="tigera"):
    if (jugador==3): 
        rta="empate"
    elif (jugador==1):
        rta= "ganaste"
    else:
        rta="perdiste"


#output
            
print("la maquina saco: " + str(maquina) + " Y " + str(rta ))


