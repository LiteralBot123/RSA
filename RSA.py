import random

a = random.randint(1,200)
b = random.randint(1,200)
n = a*b

def Euclidean(a,b):      # essentially far simplifies the two numbers to check if they are coprime
    if a == 0:
        return b
    else: 
        return Euclidean(b % a, a)

def Euler_Totient(n):      # essentially the relative primes to a number counter.
    count = 1
    for i in range(2,n):            # since Euclidean checks continuously to find lcf, if they are coprime,
        if Euclidean(1,n) == 1:     # the result will be 1
            count += 1         # counting the amount of results
        return count