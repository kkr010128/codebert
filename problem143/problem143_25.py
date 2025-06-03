num = int(input())
word = input()

for i in range(num):
    print(word[i],end="")
    if i+1 >= len(word):
        break

if len(word) > num:
    print("...")