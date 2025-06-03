n = int(input())
a = int(input())
b = int(input())

interest = b - a
min = min(a,b)
for i in range(n-2):
    f = int(input())
    if f - min > interest:
        interest = f - min
    elif f < min:
        min = f
print(interest)