a = str(input())
alpha2num = lambda c: ord(c) - ord('A') + 1
b = alpha2num(a)
c = int(b) + 1
num2alpha = lambda c: chr(c+64)
print(num2alpha(c))
