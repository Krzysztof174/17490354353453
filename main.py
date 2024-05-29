import sys
import random
import math
import numpy as np
import pandas
import matplotlib.pyplot as plt
def zad1():
    #dane = pandas.read_excel("datasets/imiona.xlsx")
    daneX = []
    daneY = []
    for i in range(1, 21):
        daneX.append(i)
        daneY.append(1/i)
    plt.plot(daneX, daneY, 'r')
    plt.plot(daneX, daneY, 'o')
    plt.axis([1, 20, 0, 1])
    plt.show()

def zad2():
    daneX = np.arange(1,21)
    daneY = 1/daneX
    plt.plot(daneX, daneY, 'g>:', label='f(x) = 1/x')
    plt.legend()
    plt.axis([0, 20, 0, 1])
    plt.show()

def zad3():
    x = np.arange(0, 31, 0.1)
    y = []
    for i in range(0, len(x)):
        y.append(math.sin(i/10))
    plt.plot(x, y, 'r', label='sin(x)')
    plt.legend()
    y = []
    for i in range(0, len(x)):
        y.append(math.cos(i/10))
    plt.plot(x, y, 'b', label='cos(x)')
    plt.legend()
    plt.axis([0, 30, -1, 1])
    plt.show()

def zad5():
    dane = pandas.read_excel("datasets/imiona.xlsx")
    dane.drop("Imie", axis=1, inplace=True)
    fig, axs = plt.subplots(1, 3)
    wyk = dane.groupby("Rok").agg({"Liczba": ["sum"]})
    wyk.plot.bar()
    wyk = dane.groupby("Plec").agg({"Plec": ["count"]})
    wyk.plot.bar()
    plt.subplots_adjust(hspace=0.5)
    plt.show()
    print(dane.head())

def zad():
    x = np.arange(-5, 6)
    y = x ** 2

    plt.plot(x, y, label='linia 1/x')
    plt.legend()
    plt.show()

#co bedzie
# x = np.arange(-5, 6)
# y = x**2
#
# plt.plot(x, y, label='linia 1/x')
# plt.legend()
# plt.show()
#
# plt.plot(y, label='linia 1/x')
# plt.legend()
# plt.show()


if __name__ == '__main__':
    #zad1()
    #zad2()
    #zad3()
    zad5()
    #zad()
