K = int(input())#asking lenght of string wanted to be shorted
S = input()#asking string

if len(S)>K:##set that S must be greater than K
    print (S[:K], "...",sep="")# to print only the K number of the string
else:
    print (S)