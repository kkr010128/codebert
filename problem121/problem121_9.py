n = int(input())
c = list('abcdefghijklmnopqrstuvwxyz')

ans = []
def calc(k):   
    if k == 0:
        return ''
    else:
        k -= 1
        return calc(k // 26) + c[k % 26]

print(calc(n))
