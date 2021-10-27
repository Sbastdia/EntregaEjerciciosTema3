from random import randint

print('Primera parte del ejercicio')

numAleatorio1= randint(1, 15)
a= int(input('Escribe un número: '))
while a!=numAleatorio1:
    if(a<numAleatorio1):
        print('El número que debe adivinar es mayor')
    elif(a>numAleatorio1):
        print('El número que debe adivinar es menor')
    a= int(input('Escribe un número: '))

print('¡ENHORABUENA, HAS ENCONTRADO EL NÚMER0!')

print('Segunda parte del ejercicio')

numAleatorio2= randint(1, 300)
i=0
b=0
while b!=numAleatorio2 and i<9:
    b= int(input("Escribe un número: "))
    if(b<numAleatorio2):
        print('El número que debe adivinar es mayor')
    elif(b>numAleatorio2):
        print('El número que debe adivinar es menor')
    i=i+1

if(b==numAleatorio2):
    print('¡ENHORABUENA, HAS ENCONTRADO EL NÚMER0!')
else:
    print('Lo siento, has pasado el número de intentos')
