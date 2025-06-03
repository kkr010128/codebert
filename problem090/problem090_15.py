S = input()


ans = 0
if S.find("RRR") >= 0:
    ans = 3
elif S.find("RR") >= 0:
    ans = 2
elif S.find("R") >= 0:
    ans = 1

    
print(ans)
