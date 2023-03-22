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
        jug="piedra"
        rta="empate"
    elif (jugador==2):
        jug="papel"
        rta= "ganaste"
    else:
        jug="tijeras"
        rta="perdiste"

if (maquina=="papel"): 
    if (jugador==2):
        jug="papel"
        rta="empate"
    elif (jugador==3):
        jug="tijeras"
        rta= "ganaste"
    else:
        jug="piedra"
        rta="perdiste"

if (maquina=="tigera"):
    if (jugador==3): 
        jug="tijeras"
        rta="empate"
    elif (jugador==1):
        jug="piedra"
        rta= "ganaste"
    else:
        jug="papel"
        rta="perdiste"


#output
            
print("la maquina saco: " + str(maquina) )
print("usted escogió: " + str(jug))
print(rta)


