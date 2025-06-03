import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    a = II()



    
    print(a + pow(a,2) + pow(a,3))

if __name__ == "__main__":
	main()