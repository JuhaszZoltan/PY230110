from time import sleep
from os import system
from random import randint

nev:str = 'Zoli'

for x in range(30):
    v:int = randint(0, 10)
    h:int = randint(0, 80)
    system('cls')
    for y in range(v): print('\n', end='')
    for z in range(h): print(' ', end='')
    print(nev)
    sleep(.5)