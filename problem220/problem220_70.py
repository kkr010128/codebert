import sys

def II(): return str(input())
def MI(): return map(int,input().split())
def MI2(): return map(str,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    S, T = MI2()
    A, B = MI()
    U = II()
    
    if U == S:
        A = A-1
    elif U == T:
        B = B-1
    
    print(A, B)

if __name__ == "__main__":
	main()