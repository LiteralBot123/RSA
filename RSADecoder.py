import random
from sympy import randprime

p = randprime(200,400)
q = randprime(200,400)
n = p*q

def Euclidean(p,q):      # essentially far simplifies the two numbers to check if they are coprime
    if p == 0:
        return q
    else: 
        return Euclidean(q % p, p)

def Euler_Totient(n):      # essentially the relative primes to a number   counter.
    count = 1
    for i in range(2,n):            # since Euclidean checks continuously to find gcf, if they are coprime,
        if Euclidean(i,n) == 1:     # the result will be 1
            count += 1         # counting the amount of results
    return count

while True:
    e = random.randint(1, Euler_Totient(n))    # generate e and see if it works in the formula
    if Euclidean(e, Euler_Totient(n)) == 1:
        e = e                   
        break               # if it works, end
    else:
        e = random.randint(1, Euler_Totient(n))     # if not, continue



Public_Key = (e,n)


# finding p and q (reverse engineering formula)
n = Public_Key(n)
if n % 2 == 0:
    p = 2
    q = n/2     # checking if divisible by even
else:
    checker = 3
    while True:         # checking if divisible by different odd numbers 
        if checker <= n:
            if n % checker == 0:
                checker = checker
            else:
                checker += 1
        else:                        # cause RSA uses two large prime numbers, 
            checker = checker        # the largest number the checker gets will be the primes


