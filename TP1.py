from ctypes import sizeof
from os import access
from random import random


import random
import math

complex = 0


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

def getPandQwithN(n):
    p = 0
    q = 0
    for i in range(2, n-1):
        if(n % i == 0):
            p = i
            q = n/p
    return {"p": int(p), "q": int(q)}

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
    print("size: ", pow( 2, size/2 ))
    return {"private": [e, n], "public": [d, n]}

    
def encrypt(message, key, type):
    messageEncrypt = pow(message, key[type][0], key[type][1])

def deciphers(message, key, type):
    messageDeciphers = pow(message, key[type][0], key[type][1])


    


if __name__ == '__main__':

    ###########################
    ####get key with size: ####
    ###########################

    # key = algorithmKey()
    # print(key)

    ###########################################
    ####chiffrer et dechiffrer le message: ####
    ###########################################

    # message = random.randint(2, key["private"][1])

    # messageEncrypt = pow(message, key["private"][0], key["private"][1])

    # messageDeciphers = pow(messageEncrypt, key["public"][0], key["public"][1])

    # print("message: ", message)

    # print("message chiffree: ", messageEncrypt)

    # print("message dechiffre: ", messageDeciphers)

    #####################################################################
    ####get message origine with the message encrypt and key public: ####
    ####################################################################

    e = 12413
    n = 13289

    pq = getPandQwithN(n)

    y = (pq["p"] - 1) * (pq["q"] - 1)

    d = modInverse(e, y)

    key = {'private':[d, n], 'public':[e, n]}

    print(key)

    messageEncrypt = int(input("Entrz le message chiffre: "))

    message = pow(messageEncrypt, key['private'][0], key['private'][1])

    messageEncrypt = pow(message, key['public'][0], key['public'][1])

    print("message: ", message)
    # print("message dechiffrer: ", messageEncrypt)


