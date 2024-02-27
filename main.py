# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
# Press the green button in the gutter to run the script.
def skrypt1():
   zdanie = input('podaj zdanie')
   ilosc = len(zdanie.split())
   print(ilosc)

def skrypt2():
   sys.stdout.write('podaj a')
   a = int(sys.stdin.readline())
   sys.stdout.write('podaj b')
   b = int(sys.stdin.readline())
   sys.stdout.write('podaj c')
   c = int(sys.stdin.readline())
   print((a**b) +c)

def skrypt3():
   palindrom = input('podaj napis')

   if(palindrom == palindrom[::-1]):
      print('jest palindromem')

   odwrotne = ''
   for i in range(0, len(palindrom)):
      odwrotne += palindrom[len(palindrom) - 1 - i]
   if(palindrom == odwrotne):
      print('jest palindromem')

def skrypt4():
   liczba = int(input('podal liczbe'))
   pierwsza = True
   if(liczba == 2):
      return print('jest liczba pierwsza')
   for i in range(2, liczba):
      if(liczba%i == 0):
         pierwsza = False
   if(pierwsza):
      print('jest liczba pierwsza')

def skrypt5():
   licznik = 1
   while licznik != 1000:
      dzielniki = []
      for i in range(1, licznik):
         if licznik%i == 0:
            dzielniki.append(i)
      suma = 0
      for i in range(0, len(dzielniki)):
         suma += dzielniki[i]
      if suma == licznik:
         print(licznik)
      licznik += 1

def skrypt6():
   lista = [2, 5.4, 6, 6.7]
   nowa_lista = []
   for i in lista:
      nowa_lista.append(i**2)
   print(nowa_lista)

def skrypt7():
   licznik = 0
   lista = []
   while licznik != 10:
      a = int(input('podaj liczbe'))
      if a%2 == 0:
         lista.append(a)
      licznik += 1
   print(lista)

def skrypt8():


if __name__ == '__main__':
   #skrypt1()
   #skrypt2()
   #skrypt3()
   #skrypt4()
   #skrypt5()
   #skrypt6()
   #skrypt7()
   skrypt8()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
