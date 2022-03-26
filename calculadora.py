def suma(a, b):
    return (a+b)


def multiplica(a, b):
    return(a*b)


def resta(a, b):
    return (a-b)


def divide(a, b):
    return(a/b)

def pedirnum():
    num1= int(input('Ingrese un numero: '))
    return(num1)

      
menu="""

MENU


1-Sumar

2-Restar

3-Multiplicar

4-Dividir

"""

print(menu)
operacion=int(input('Elija una operacion: '))


if operacion == 1:
    print(suma(pedirnum(),pedirnum()))
elif operacion == 2:
    print(resta(pedirnum(),pedirnum()))
elif operacion == 3:
   print(multiplica(pedirnum(),pedirnum()))
elif operacion == 4:
    print (divide(pedirnum(),pedirnum()))
else:
    print('Esa operacion no es correcta')

