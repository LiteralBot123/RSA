import matplotlib as m
import time
from RSA import All_Together, Encryption, Encryption_Take_Input, Decryption
from RSADecoder import Find_P_And_Q, Encryption, Decryption
import random

def RSADecoder_Time():
    while True:
        count = 1
        RSADecoder_Vals = []
        if count <= 100:
            All_Together()
            Encryption()
            RSADecoder_Start = time.time()
            Find_P_And_Q()
            RSADecoder_End = time.time()
            RSADecoder_Time_Taken = RSADecoder_End - RSADecoder_End
            RSADecoder_Vals.append(RSADecoder_Time_Taken)
            return RSADecoder_Vals


def RSA_Time():
    while True:
        count = 1
        RSA_Vals = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        word = []
        if count <= 100:
            for i in range(count):
                randomletter = random.choice(letters)
                word.append(randomletter)
                RSA_Start = time.time()
                All_Together()
                Encryption_Take_Input(word)
                RSA_End = time.time()
                RSA_Time_Taken = RSA_End - RSA_Start
                RSA_Vals.append(RSA_Time_Taken)
                return RSA_Vals

print(RSA_Time())




m.plot()

