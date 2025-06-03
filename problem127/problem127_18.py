# Crane and Turtle

X, Y = [int(i) for i in input().split()]

for t in range(0, X + 1):
    legs = 2 * (X + t)
    if Y == legs:
        a = 'Yes'
        break
    if Y < legs:
        a = 'No'
        break
else:
    a = 'No'

print(a)
