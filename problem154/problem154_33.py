# coding: utf-8
# Your code here!
def main():
    n, k = map(int, input().split())
    
    a = []
    for i in range(k):
        d = int(input())
        tmp_a = list(map(int, input().split()))
        a.extend(tmp_a)
    ans = len(set(range(1, n+1)) - set(a))
    print(ans)
    
main()
