import sys
import random
import math

def zad1():
    A = [1-x for x in range(1, 11)]
    B = [4**i for i in range(0,8)]
    C = [x for x in B if x%2 == 0]
    print(A, B, C)

def zad2():
    listy1 = []
    for i in range(1, 11):
        listy1.append(math.floor(10*random.random()))
    listapar = [i for i in listy1 if i%2 == 0]
    print(listapar)

def zad3():
    produkty = {"mleko": "litr", "jajka": "sztuka", "mieso": "kg", "batony": "sztuka"}
    sztuki = { k:v for k,v in produkty.items() if v == "sztuka"}
    print(sztuki)

def zad4(a, b, c):
    if (a**2 + b**2) == c**2:
        print("jest trojkatny")
        return
    if (a**2 + c**2) == b**2:
        print("jest trojkatny")
        return
    if (b**2 + c**2) == a**2:
        print("jest trojkatny")
        return
    print("nie jest trojkatny")
    
def zad5(a=3, b=5, h=3):
    print("pole trapezu: ", (a+b)*h/2)

def zad6(a=1, b=4, ile=10):
    iloczyn = 1;
    for i in range(1, ile):
        iloczyn = iloczyn * a * b**i
    print(iloczyn)

def zad7():
    liczba = int(input("podaj liczbe: "))
    try: {
    print("pierwiastek: ", math.sqrt(liczba))
    }
    except: {
    print("pierwiastek ujemny")
    }
    
if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4(6,8,10)
    zad5()
    zad6()
    zad7()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
