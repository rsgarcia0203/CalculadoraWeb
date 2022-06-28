import math


def suma(n,m):
    return n+m


def resta(n,m):
    return n-m


def multiplicacion(n,m):
    return n*m


def division(n,m):
    return n/m


def modulo(n,m):
    return n%m


def potencia(n,m):
    return n**m


def raiz(n):
    return n**0.5
     

def raiz_de_M(n,m):
    return n**(1/m)


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


def combinaciones(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))


def permutaciones(n,m):
    return factorial(n)/factorial(n-m)


def binomial(n,m):
    return combinaciones(n,m)/factorial(m)


def binomial_inverso(n,m):
    return factorial(n)/(factorial(n-m)*factorial(m))


def coseno(n):
    return math.cos(n)


def seno(n):
    return math.sin(n)


def tangente(n):
    return math.tan(n)


def coseno_inverso(n):
    return math.acos(n)


def seno_inverso(n):
    return math.asin(n)


def tangente_inverso(n):
    return math.atan(n)


def logaritmo(n):
    return math.log(n)


def logaritmo_base(n,m):
    return math.log(n,m)


def exponencial(n):
    return math.exp(n)


def pi():
    return math.pi


def e():
    return math.e


def seno_grados(n):
    return math.sin(math.radians(n))


def coseno_grados(n):
    return math.cos(math.radians(n))


def tangente_grados(n):
    return math.tan(math.radians(n))


def seno_grados_inverso(n):
    return math.degrees(math.asin(n))


def coseno_grados_inverso(n):
    return math.degrees(math.acos(n))


def tangente_grados_inverso(n):
    return math.degrees(math.atan(n))


def sumatoria(n):
    return sum(range(n+1))


def sumatoria_inverso(n):
    return sum(range(n,0,-1))

