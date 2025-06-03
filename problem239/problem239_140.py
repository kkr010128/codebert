c = input()
alpha = [chr(i) for i in range(97, 97+26)]
number = alpha.index(c)
print(alpha[number + 1])
