k = int(input())
a,b = map(int, input().split())

def judge(a,b):
    for i in range(a,b+1):
        if i%k == 0: return 'OK'
    return 'NG'

print(judge(a,b))