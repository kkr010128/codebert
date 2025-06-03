N = input()

answer = 0
for keta in N:
    answer = (answer + int(keta))%9
if not answer:
    print("Yes")
else:
    print("No")
