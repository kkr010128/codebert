#153
def main():
    N, K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort()
    H.reverse()
    H = H[K:]
    cost = 0
    for i in H:
        cost+=i
    print(cost)
main()