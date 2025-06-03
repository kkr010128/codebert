list1 = input().split(' ')
list1 = list(map(int, list1))
a = list1[0]
b = list1[1]
c = list1[2]

divisor = []
answer = []

for index in range(0, c):
    index += 1
    if c % index == 0:
        divisor.append(index)

for test_digit in range(a, b + 1):
    if test_digit in divisor:
        answer.append(test_digit)

print(len(answer))