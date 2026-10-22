import matplotlib.pyplot as plt
import time
from RSA import Get_Factors
from RSADecoder import All_Together, RSA_Decoding
import random



Creating_Factors = Get_Factors()
All_Together()
Decoding_Factors = RSA_Decoding()



x = [1, 2, 3, 4, 5]



plt.figure(figsize = (6, 6))
plt.plot(x, Creating_Factors, label = 'Time taken to create factors p and q')
plt.plot(x, Decoding_Factors, label = 'Time taken to decode factors p and q')



plt.xlabel('Input size: (digits)')
plt.ylabel('Time taken per digit: ')
plt.legend()
plt.show()