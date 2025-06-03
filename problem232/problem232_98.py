import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    a, b = MI()
    L = sorted([a, b])
    if L[0] == a:
        ans = int(str(a)*b)
    else:
        ans = int(str(b)*a)
    print(ans)


    
    

if __name__ == "__main__":
	main()