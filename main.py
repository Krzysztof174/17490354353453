import sys
import random
import math
import numpy as np
def zad1():
    a = np.array([3*i for i in range(1, 16)])
    print(a)

def zad2():
    a = []
    for i in range(1, 10):
        a.append(i/10)
    b = np.fromiter(a, dtype='int64')
    print(b)

def zad3(n):
    a = np.arange(1, 101)
    b = a.reshape(10, 10)
    aa = np.zeros((n*n), dtype='int32')
    return b

def zad4(x, n):
    a = np.logspace(1,n, num =n, base=x)
    print(a)

def zad5(n):
    a = np.arange(n, 0, -1)
    diag = np.diag(a)
    return diag

def zad6():
    mrowka = np.array(list('mrowka'))
    wykreslanka = np.diag(mrowka)
    wykreslanka[:, 0] = mrowka
    for a in range(5):
        wykreslanka[a, a] = mrowka[a]
    print(wykreslanka)

def zad7(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2 + (2 * i) for _ in range(n - i)], k=i)
        mac += np.diag([2 + (2 * i) for _ in range(n - i)], k=-i)

def zad8(tab, kierunek = 'poziomo'):
    if kierunek == 'poziomo':
        if tab.shape[0]%2 != 0:
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0] / 2), :]
        print(p1)
        print(p2)
    elif kierunek == 'pionowo':
        if tab.shape[1]%2 != 0:
            p1 = tab[0:int(tab.shape[0]/2), :]
            p2 = tab[int(tab.shape[0] / 2), :]
    print(p1)
    print(p2)

def zad9(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return zad9(n-1) + zad9(n-2)

def zad10():
    a = np.arange(12).reshape((3, 4))
    print(a.sum())

if __name__ == '__main__':
    zad1()
    zad2()
    print(zad3(10))
    zad4(2, 4)
    print(zad5(5))
    zad6()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
