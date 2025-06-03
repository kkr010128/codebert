S = input()
if S == 'RRR':
    print(3)
elif S == 'SSS':
    print(0)
elif S=='RSS' or S == 'SRS' or S=='SSR' or S=='RSR':
    print(1)
else:
    print(2)