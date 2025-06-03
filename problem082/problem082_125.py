str1 = list(input())
str2 = list(input())

answer = len(str2)
for i in range(len(str1)-len(str2)+1):
    count = 0

    for j in range(len(str2)):
        if not str1[i+j] == str2[j]:
            count += 1

    if count < answer:
        answer = count

print(answer)
