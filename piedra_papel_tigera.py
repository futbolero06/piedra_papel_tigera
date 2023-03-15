# programa para simular el lanzamiento de un dado

import random

print("------------------------------------------")
print("---------LANZAMIENTO DE UN DADO----------")
print("------------------------------------------")

# input 

# processing

maquina = random.randint(1,3)

# usuario = random.randint(1,3)

jugador= int(input("escoje que sacaras:"))

if (maquina==1): #piedra
    if (jugador==1):
        rta="empate"
    elif (jugador==2):
        rta= "ganaste"
    else:
        rta="perdiste"

    rta = "PIEDRA"
elif (usuario==2):
    rta = "PAPEL"
elif (usuario==3):
    rta = "TIGERA"
else:
    rta = ""


if (d2>6):
    rta = "usted digito un numero no valido"
else: 
    if (d1==d2):
        rta = "ADIVINASTE EL NUMERO"
    else:
        rta = "I AM SORRY..... NO ADIVINASTE"