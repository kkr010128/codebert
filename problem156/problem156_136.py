import math

X= int(input())

for A in range(-120,121):
    for B in range(-120,A+1):
        if A**5-B**5  == X:
            print(A,B)
            exit()