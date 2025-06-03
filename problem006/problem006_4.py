n = int(input())
S = 100000

for i in range(n):
    S = int(S*1.05)
    slist = list(str(S))
    if slist[-3:] == ['0','0','0'] :
        S = S
    else:
        S = S  - int(slist[-3])*100 - int(slist[-2])*10 - int(slist[-1])*1 + 1000

print(S)
