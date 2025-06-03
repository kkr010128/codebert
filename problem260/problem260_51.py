A, B, C = map(int, input().split())
if A+B+C >= 22:
    print('bust')
elif A+B+C <=21:
    print('win')