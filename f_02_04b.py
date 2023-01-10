from time import sleep
from os import system

nev:str = 'Zoli'
for x in range(30):
    for y in range(x): print(' ', end='')
    print(nev)
    sleep(.5)
    system('cls')