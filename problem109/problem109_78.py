N = int(input())
x = []
for _ in range(N):
    s = input()
    x.append(s)
print('AC'+ ' '+ 'x'+ ' '+str(x.count('AC')))
print('WA'+ ' '+ 'x'+ ' '+str(x.count('WA')))
print('TLE'+ ' '+ 'x'+ ' '+str(x.count('TLE')))
print('RE'+ ' '+ 'x'+ ' '+str(x.count('RE')))