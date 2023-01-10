from time import sleep
from os import system

ido = 10
system('cls')
for x in range(ido):
    print(f'{ido - x}', end='')
    for y in range(3):
        print('.', end='')
        sleep(.3)
    sleep(.3)
    system('cls')
print('lejárt az idő, viszont látásra!')
sleep(3)
system('cls')