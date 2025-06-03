x = input()
alpha2num = lambda c: ord(c) - ord('a') + 1
num2alpha = lambda c: chr(c+96+1)
a = alpha2num(x)
b = num2alpha(a)
print(b)