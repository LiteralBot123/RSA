# setting the actual values as the previous code did
import random
import time
from sympy import randprime



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

def E_Generation(Totient):
    while True:
        e = random.randint(1, Totient)    # generate e and see if it works in the formula
        if Euclidean(e, Totient) == 1:
            e = e                   
            return e               # if it works, end
        else:
            e = random.randint(1, Totient)     # if not, continue


def D_Generation(e, Totient):
#d * e % Euler_Totient(n) = 1 rearranged
    d = 1
    while True:
        if (d*e) % Totient != 1:
            d += 1
        else:
            d = d
            return d

p = randprime(200,400)
q = randprime(200,400)
n = p * q
Totient = Euler_Totient(n)

e = E_Generation(Totient)
d = D_Generation(e, Totient)
Public_Key = (e,n)
Private_Key = (d,n)

# actually computing and decoding with only public key as info



# finding p and q (reverse engineering formula)
def Find_P_And_Q(n_To_Find):
    if n_To_Find % 2 == 0:
        p = 2
        q = int(n/2)     # checking if divisible by even
    else:
        checker = 3
        while True:         # checking if divisible by different odd numbers 
            if checker <= n_To_Find:
                if n_To_Find % checker == 0:
                    checker = checker
                    return checker
                else:
                    checker += 2
            else:                        # cause RSA uses two large prime numbers, 
                checker = checker        # the largest number the checker gets will be the primes
                return n_To_Find





def All_Together():         # purely for the graphing later on 
    p_Graphed = randprime(200,400)
    q_Graphed = randprime(200,400)
    n_Graphed = p_Graphed * q_Graphed
    Totient_Graphed = Euler_Totient(n_Graphed)
    e_Graphed = E_Generation(Totient_Graphed)
    d_Graphed = D_Generation(e_Graphed, Totient_Graphed)
    return d_Graphed, e_Graphed, n_Graphed



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



def RSA_Decoding():
    count = 1
    factors = 10
    RSADecoder_Vals = []
    p_Decode = randprime(2, factors)
    q_Decode= randprime(2, factors)
    n_Decode = p_Decode * q_Decode
    while count <= 5:
        All_Together()
        RSADecoding_Start = time.time()
        Find_P_And_Q(n_Decode)
        RSA_Decoding_End = time.time()
        RSA_Decoding_Time_Taken = RSA_Decoding_End - RSADecoding_Start
        RSADecoder_Vals.append(RSA_Decoding_Time_Taken)
        factors *= 10
        count += 1
        p_Decode = randprime(1, factors)
        q_Decode = randprime(1, factors)
        n_Decode = p_Decode * q_Decode
    print(RSADecoder_Vals)
    return RSADecoder_Vals



RSA_Decoding()