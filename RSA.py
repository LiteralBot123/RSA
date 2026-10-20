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

#d * e % Euler_Totient(n) = 1 rearranged
Totient = Euler_Totient(n)   # in variable so doesn't have to recompute constantly

d = 1
while True:
    if (d*e) % Totient != 1:
        d += 1
    else:
        d = d
        break



Public_Key = (e,n)
Private_Key = (d,n)



print(Public_Key, Private_Key)



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



def Decryption(Encrypted_Text):
    global d
    global n
    Decrypted_Message = []      # string so it looks good when decoded and not list format
    for i in Encrypted_Text:    # for each number value
        Decrypted_Value = pow(i,d,n)    # use formula plaintext = ciphertext^d % n
        Decrypted_Message.append(chr(Decrypted_Value))
    print(Decrypted_Message)
    return(Decrypted_Message)
    


run = Encryption()
Decryption(run)