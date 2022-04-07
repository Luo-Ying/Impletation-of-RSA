from ctypes import sizeof
from os import access
from random import random


import random
import math


# verify if the value is prime number
def verifPrimeNumber(value):
    if (value > 1):
        for i in range(2, int(value/2)+1):
            if (value % i == 0):
                return False
    return True

# define value random
def defineValue(size):
    value = random.randint(2, int(size))
    while ( verifPrimeNumber(value) == False ):
        value = random.randint(2,int(size))
    return value

def pgcd(e, y):
    pgcd = 0
    while (e != y): 
        pgcd = abs(y - e) 
        y = e 
        e = pgcd 
    return pgcd

def modInverse(e, y):
    for x in range (1, y):
        if (((e%y) * (x%y)) % y == 1):
            return x

def algorithmKey():
    size = int(input("Entrez la taille: "))
    while(size <= 3):
        size = int(input("Entrez la taille(la taille doit etre superieur a 3): "))
    p = defineValue(pow( 2, size/2 ))
    q = defineValue(pow( 2, size/2 ))
    while(p == q):
        q = defineValue(pow( 2, size/2 ))
    # print(p, q)

    n = p * q
    y = (p - 1)*(q - 1)
    e = random.randint(2, y)
    # quand pgcd == 1, p et q sont premier entre eux
    while(pgcd(e, y) != 1):
        e = random.randint(2, y)
    # d * e = 1 (mod y)
    d = modInverse(e, y)
    while(e == d):
        e = random.randint(2, y)
        while(pgcd(e, y) != 1):
            e = random.randint(2, y)
        d = modInverse(e, y)
    return {"private": [e, n], "public": [d, n]}

    
def encrypt(message, key, type):
    messageEncrypt = math.pow(message, key[type][0]) % key[type][1]

    


if __name__ == '__main__':

    key = algorithmKey()
    print(key)

    message = random.randint(2, key["private"][1])

    messageEncrypt = pow(message, key["private"][0], key["private"][1])

    messageDeciphers = pow(messageEncrypt, key["public"][0], key["public"][1])

    print("message: ", message)

    print("message chiffree: ", messageEncrypt)

    print("message dechiffre: ", messageDeciphers)

