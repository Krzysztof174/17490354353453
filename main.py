import sys
import random
import math

def zad1():
    print( round(( math.e**4 - math.log2(34) )**(1/3), 2))
    print( round(( math.log(20) + math.cos(45) + math.e )**(1/3), 2))
    print( round(( math.log(20, 3) + math.sin(45) * 5/8 )**(1/4), 2))
    print( round(math.log(23, 3) + (math.sin(45) +5)**(1/3), 2) )
    print(round( ( math.log(32, 2) + math.pi + math.sin(56) )**(1/4), 2))

def zad2():
    wysokosc = 0
    try:
        wysokosc = int(input("podaj wysokosc wiezy"))
    except:
        print("trzeba podac liczbe")
        wysokosc = 0
    if(wysokosc == 0):
        return
    if(wysokosc > 10):
        return print("zbyt duza wysokosc") 
    for i in range(1, wysokosc +1):
        print("A"*i)

def zad3():
    wysokosc = 0
    try:
        wysokosc = int(input("podaj wysokosc wiezy"))
    except:
        print("trzeba podac liczbe")
        wysokosc = 0
    if(wysokosc == 0):
        return
    if(wysokosc > 10):
        return print("zbyt duza wysokosc")
    for i in range(1, wysokosc + 1):
        print(round(wysokosc - i) * " " + "A"*i + "A" * (i-1))

def zad5(n):
    wektor = []
    for i in range(0, n):
        wektor.append([])
        for z in range(0, n):
            wektor[i].append(int(round(10*random.random(), 0)))
    print(wektor)
    for i in range(0, n):
        suma = 0
        for z in range(0, n):
            suma += wektor[i][z]
        print(suma)
if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad5(6)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
