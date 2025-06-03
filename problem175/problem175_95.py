n = int(input())
s = input()

al=s.count("R")*s.count("G")*s.count("B")

for i in range(n-2):
    for k in range(i+1,n-1):
        l=k+(k-i)
        if l>=n:
            continue
        if s[i]!=s[k] and s[i]!=s[l] and s[k]!=s[l]:
            al-=1

print(al)
