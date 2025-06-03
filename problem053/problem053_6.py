n = input()
a = list(map(lambda x : int(x), input().split(" ")))
for i, a_ in enumerate(reversed(a)):
    if i == 0:
        print("%d" % a_, end="")
    else:
        print(" %d" % a_, end="")
print()