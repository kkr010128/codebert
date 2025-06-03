a, b = [int(i) for i in input().split(' ')]
answer1 = a // b
answer2 = a % b
answer3 = round(float(a) / float(b), 5)
print(answer1, answer2, answer3)
