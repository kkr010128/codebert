import random as random

s=input()
s_=s[:-2]

s1=random.choice(s_)
l=s_.index(s1)
s2=s[l+1]
s3=s[l+2]
s4=s1+s2+s3

print(s4)