d = {chr(i):i-96 for i in range(97,123)}
D = {val:key for key,val in d.items()}
N = int(input())
x = ""
while N>0:
    a = N%26
    if a!=0:
        x += D[a]
        N = N//26
    else:
        x += "z"
        N = N//26
        N -= 1
print(x[::-1])