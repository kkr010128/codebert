
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    if S[-1]=="s":
        S+="es"
    else:
        S+="s"
        
    print(S)

main()
