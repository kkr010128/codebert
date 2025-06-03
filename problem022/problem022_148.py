len_s = int(input())
s = [int(i) for i in input().split()]
len_t = int(input())
t = [int(i) for i in input().split()]
cnt = 0

for f in t:
    i = 0
    while i < len(s) and s[i] != f:
        i += 1
    if i < len(s):
        cnt +=1
print(cnt)