n, p = (int(i) for i in input().split());

s = input();

if p == 2 or p == 5:
    res = 0;
    for i in range(len(s)):
        if int(s[i]) % p == 0:
            res += i + 1;
    print(res);
    exit(0);

h = [0 for i in range(len(s) + 1)];
st = 1;

for i in range(len(s) - 1,-1,-1):
    #print(i);
    h[i] = (st * int(s[i]) + h[i + 1]) % p;
    st = (st * 10) % p;

#print(h);

h.sort();

#print(h);

i = 0;
res = 0;

while i <= n:
    j = i;
    while j + 1 <= n and h[i] == h[j + 1]:
        j += 1;
    l = j - i + 1;
    res += (l * (l - 1)) // 2;
    i = j + 1;

print(res);
