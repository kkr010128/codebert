num = int(input())
numbers = list(map(int,input().split()))

for i in reversed(numbers):
    print(i,end="")
    if i != numbers[0]:
        print(" ",end="")
print()
