from random import randint

numAleatorio1= randint(1, 15)

a= input()
while a!=numAleatorio1:
    if(a<numAleatorio1):
        print('El número que debe adivinar es mayor')
    elif(a>numAleatorio1):
        print('El número que debe adivinar es menor')
    a= int(input())

print('¡ENHORABUENA, HAS ENCONTRADO EL NÚMER0!')



