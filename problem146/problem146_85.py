from math import gcd
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
mod = 1000000007

#%%

kai = [1]*(n+1)
gyaku = [1]*(n+1)

for i in range(2, n+1):
    kai[i] = kai[i-1]*i % mod
    gyaku[i] = gyaku[i-1]*pow(i, mod-2, mod) %mod

azero = 0
bzero = 0
zerozero = 0
dict_patterns = {}
dict_patterns_minus = {}
all_effective = 0
answer = 0
dict_patterns["1,0"] = 0
dict_patterns["0,-1"] = 0

for i in range(n):
    minus = False
    a, b = ab[i]
    if a == 0 and b == 0:
        zerozero += 1
        continue
    elif b == 0:
        dict_patterns["1,0"] += 1
        continue
    elif a == 0:
        dict_patterns["0,-1"] += 1
        continue
    
    common = gcd(a,b)
    a = a//common
    b = b//common
    
#%%
    
    if a < 0 and b < 0:
        a = -a
        b = -b
    elif a < 0:
        a = -a
        b = -b
    
    
    to_str = str(a)+","+str(b)
    if to_str not in dict_patterns:
        dict_patterns[to_str] = 1
    else:
        dict_patterns[to_str] += 1


keys = list(dict_patterns.keys())
patterns = []
test = []
for i in range(len(keys)):
    pattern_A = dict_patterns[keys[i]]
    dict_patterns[keys[i]] = 0
    pattern_B = 0
    a, b = map(int, keys[i].split(","))
    
    if str(b)+","+str(-a) in dict_patterns:
        pattern_B += dict_patterns[str(b)+","+str(-a)]
        dict_patterns[str(b)+","+str(-a)] = 0
    if str(-b)+","+str(a) in dict_patterns:
        pattern_B += dict_patterns[str(-b)+","+str(a)]
        dict_patterns[str(-b)+","+str(a)] = 0
    if pattern_A != 0 or pattern_B != 0:
        patterns.append(max(2**pattern_A-1,0) + max(2**pattern_B-1,0)+1)  
    test.append([pattern_A, pattern_B])

answer = 1
for i in range(len(patterns)):
    answer = answer*patterns[i] % mod

print((answer-1+zerozero)%mod)

