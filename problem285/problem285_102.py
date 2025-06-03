S = input()
S = S.replace('><','>,<').split(',')

ans = 0

for s in S:
    small = s.count('<')
    big = s.count('>')
    tmp = max(small,big)\
        + (max(small,big)-1)*max(small,big)//2\
        + (min(small,big)-1)*min(small,big)//2
    ans += tmp
print(ans)