#!/usr/bin/env python3
import random
import sys
from math import *

n1=10000000000000431000000000002257
n2=10000000000000989000000000007189
n3=10000000000002351000000000089947
e = 3
msg = input("Message to be encrypted: \n")
msg_int=0
#Encode the message
for i in range(len(msg)):
	msg_int=msg_int|(ord(msg[len(msg)-i-1])<<(8*(len(msg)-i-1)))
print(msg_int)

#encrypt with RSA but using wolframalpha
#c1=msg_int**e % n1
#c2=msg_int**e % n2
#c3=msg_int**e % n3

#Results:
#c1=6945603062832422854388886096396
#c2=5425415319495558266762677460599
#c3=8609349954899401334728474476494
