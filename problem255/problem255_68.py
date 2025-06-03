n = int(input())
s,t = list(map(str,input().split()))
string = []
for i in range(len(s)):
    string.append(s[i])
    string.append(t[i])
print(''.join(string))