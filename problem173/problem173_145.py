N = int(input())

def S(x):
    return(x*(x+1)//2)

print(S(N) - 3*S(N//3) - 5*S(N//5) + 15*S(N//15))