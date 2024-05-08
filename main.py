import sys
import random
import math
import numpy
import pandas
def zad1():
    dane = pandas.read_excel("datasets/imiona.xlsx")
    return dane

def zad2():
    dane = zad1()
    #print(dane)
    #print(dane[dane["Liczba"] > 1000])
    #print(dane[dane["Imie"] == "KRZYSZTOF"])
    #print(dane.groupby("Rok").sum("Liczba"))
    #print(dane[(dane["Rok"] <= 2005) & (dane["Rok"] >= 2000)].sum()["Liczba"])
    #print(dane[dane["Plec"] == "M"].sum()["Liczba"])
    #print(dane[dane["Plec"] == "K"].sum()["Liczba"])


if __name__ == '__main__':
    zad2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
