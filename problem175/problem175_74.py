n = int(input())
s = input()
#print(s)

tot = s.count('R') * s.count('G') * s.count('B')
#print(tot)

for i in range(n):
    for d in range(1,n):
        j = i+d
        k = j+d
        if k > n-1:
            break
        if s[i]!=s[j]!=s[k]!=s[i]:
            tot -= 1

print(tot)