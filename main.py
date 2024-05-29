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
    #print(dane.sum()["Liczba"])
    #print(dane[(dane["Rok"] <= 2005) & (dane["Rok"] >= 2000)].sum()["Liczba"])
    #print(dane[dane["Plec"] == "M"].sum()["Liczba"])
    #print(dane[dane["Plec"] == "K"].sum()["Liczba"])
    #print(dane.groupby(["Rok", "Plec"]).head(1))
    #print(dane.groupby(["Imie", "Plec"]).sum().sort_values("Liczba").tail(2))

def zad3():
    dane = pandas.read_csv("datasets/zamowienia.csv", sep=";", delimiter=None, decimal='.')
    #1

    #2
    #print(dane.sort_values(by="Utarg").tail(5))
    #3
    #print(dane["idZamowienia"].value_counts())


if __name__ == '__main__':
    zad2()
    zad3()
