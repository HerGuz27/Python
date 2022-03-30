from operator import truediv
from numpy import True_


questions = [
    "What colors are apples?\n(a) Red\n(b) Purple\n(C) Orange\n\n",
    "What colors are oranges?\n(a) Red\n(b) Purple\n(C) Orange\n\n",
    "What colors are grapes?\n(a) Red\n(b) Purple\n(C) Orange\n\n"
]


i = 0
isbool = True


while ((i <= 2) and (isbool == True)):
    print(questions[i])
    opcion1 = input("Elija su opcion: ")

    if (opcion1 == 'a'):
        i = i+1
        print(questions[i])
    else:
        print('Respuesta Incorrecta')
        isbool = False
        break

    opcion2 = input("Elija su opcion: ")
    if (opcion2 == 'c'):
        i = i+1
        print(questions[i])
    else:

        print('Respuesta Incorrecta')
        isbool = False
        break
    opcion3 = input("Elija su opcion: ")
    if (opcion3 == 'b'):
        i = i+1
        
    else:

        print('Respuesta Incorrecta')
        i=3
        isbool = False
        break

if (isbool):
    print('Ganaste')
else:
    print('Perdiste')