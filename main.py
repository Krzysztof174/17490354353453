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
    return b

def zad4(x, n):
    a = np.logspace(1,n, num =n, base=x)
    print(a)

def zad5(n):
    a = np.arange(n,0, -1)
    print(a)
    b = np.diagonal([a, a])
    print(b)

def zad6():
    a = np.array([['a', 'l', 'a'], ['', 'ó', ''], []], dtype=bytes)
    print(a)

if __name__ == '__main__':
    zad1()
    zad2()
    print(zad3(10))
    zad4(2, 4)
    zad5(5)
    zad6()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
