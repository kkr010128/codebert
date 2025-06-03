def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

S = input()

if S[len(S) - 1] == "s":
    S += "es"
else:
    S += "s"
    
print(S)