{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #encoding:UTF-8\
import random\
\
while True: \
    aleatorio = random.randrange(0, 3)\
    elijePc = ""\
    print("1)Piedra")\
    print("2)Papel")\
    print("3)Tijera")\
    print("4)Salir del Programa")\
    opcion = int(input("Que eliges: "))\
    \
    if opcion == 1:\
        eligeUsuario = "piedra"\
    elif opcion == 2:\
        eligeUsuario = "papel"\
    elif opcion == 3:\
        eligeUsuario = "tijera"\
    elif opcion == 4:\
        print ("Nos vemos!")\
        break\
    else:\
        print ("Valor Invalido")\
        continue\
        \
    print("Tu eliges: ", eligeUsuario)   \
    if aleatorio == 0:\
        eligePc = "piedra"\
    elif aleatorio == 1:\
        eligePc = "papel"\
    elif aleatorio == 2:\
        eligePc = "tijera"\
    print("PC eligio: ", eligePc)\
    print("...")\
    \
    if eligePc == "piedra" and eligeUsuario == "papel":\
        print("Ganaste, papel envuelve piedra")\
    elif eligePc == "papel" and eligeUsuario == "tijera":\
        print("Ganaste, tijera corta papel")\
    elif eligePc == "tijera" and eligeUsuario == "piedra":\
        print("Ganaste, piedra pisa tijera")\
        \
    if eligeUsuario == "piedra" and eligePc == "papel":\
        print("Perdiste, papel envuelve piedra")\
    elif eligeUsuario == "papel" and eligePc == "tijera":\
        print("Perdiste, tijera corta papel")\
    elif eligeUsuario == "tijera" and eligePc == "piedra":\
        print("Perdiste, piedra pisa tijera")\
    elif eligePc == eligeUsuario:\
        print("Empate")\
    again = input("Jugamos de nuevo? Si/No: ")\
    if 'si' in again:\
        continue\
    elif 'no' in again:\
        print("Nos vemos!")\
        break\
    else:\
        print("Valor Invalido")}