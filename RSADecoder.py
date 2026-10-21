# setting the actual values as the previous code did
import random
import time
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






# actually computing and decoding with only public key as info



# finding p and q (reverse engineering formula)
def Find_P_And_Q():
    n = Public_Key[1]
    if n % 2 == 0:
        p = 2
        q = int(n/2)     # checking if divisible by even
    else:
        checker = 3
        while True:         # checking if divisible by different odd numbers 
            if checker <= n:
                if n % checker == 0:
                    checker = checker
                    return checker
                else:
                    checker += 2
            else:                        # cause RSA uses two large prime numbers, 
                checker = checker        # the largest number the checker gets will be the primes
                return checker


checker = Find_P_And_Q()
p = checker
q = int(n / p)



def E_Generation():
    while True:
        e = random.randint(1, Euler_Totient(n))    # generate e and see if it works in the formula
        if Euclidean(e, Euler_Totient(n)) == 1:
            e = e                   
            return e               # if it works, end
        else:
            e = random.randint(1, Euler_Totient(n))     # if not, continue


def D_Generation():
#d * e % Euler_Totient(n) = 1 rearranged
    Totient = Euler_Totient(n)   # in variable so doesn't have to recompute constantly
    d = 1
    while True:
        if (d*e) % Totient != 1:
            d += 1
        else:
            d = d
            return d



def All_Together():         # purely for the graphing later on 
    p = randprime(200,400)
    q = randprime(200,400)
    n = p*q
    Euler_Totient(n)
    E_Generation()
    D_Generation()
    return d, e, n


d = D_Generation()
Private_Key = (d,n)



# message encryption
def Encryption():           
    global e        # takes from outside
    global n
    Encrypted_Message = []
    Message = input('What message do you wish to be encoded and sent? ')
    for i in Message:
        i = ord(i)
        Encrypted_Value = pow(i,e,n)            # formula to encrypt
        Encrypted_Message.append(Encrypted_Value)
    print(Encrypted_Message)                    # print out the message getting sent
    return Encrypted_Message

# time to see if it works by attempting to decrypt it
def Decryption(Encrypted_Text):
    global d
    global n
    Decrypted_Message = []      # string so it looks good when decoded and not list format
    for i in Encrypted_Text:    # for each number value
        Decrypted_Value = pow(i,d,n)    # use formula plaintext = ciphertext^d % n
        Decrypted_Message.append(chr(Decrypted_Value))
    print(Decrypted_Message)
    return(Decrypted_Message)



Ciphertext = Encryption()
Decryption(Ciphertext)



def RSADecoding():
    count = 1
    factors = 10
    RSADecoder_Vals = []
    p = randprime(1, factors)
    q = randprime(1, factors)
    n = p *q
    while count <= 10:
        RSADecoding_Start = time.time()
        Find_P_And_Q()
        RSA_Decoding_End = time.time()
        RSA_Decoding_Time_Taken = RSA_Decoding_End - RSADecoding_Start
        RSADecoder_Vals.append(RSA_Decoding_Time_Taken)
        factors *= 10
        count += 1
    print(RSADecoder_Vals)
    return RSADecoder_Vals



RSADecoding()