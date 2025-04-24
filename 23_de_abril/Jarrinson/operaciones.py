'''
Crear las funciones suma,resta, multiplicación, division
(Validad 0 denominador), division piso
crear una funcion que genere un numero aleatorio (import ramdon)
crear una funcion modulo
'''


def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    if b==0:
        return "No se puede dividir por cero"
    return a/b


def division_piso (a,b):
    return a//b