X, Y = list(map(int, input().split()))

crane = 2*X - Y/2
turtle = Y/2 - X

print(['No', 'Yes'][crane >= 0 and turtle >= 0 and abs(crane) + abs(turtle) > 0 and Y % 2 == 0])