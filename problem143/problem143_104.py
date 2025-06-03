k = int(input())
s = input()
a = len(s) - k
if a <= 0:
    print(s)
else:
    #a >0
    print(s[:k] + "...")
