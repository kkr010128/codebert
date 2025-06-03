s = str(input())
if s.count('RRR') == 1:
    print(3)
elif s.count('RR') == 1:
    print(2)
elif 1 <= s.count('R'):
    print(1)
else:
    print(0)