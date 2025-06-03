W = input().rstrip()
lst = []
while True:
    line = input().rstrip()
    if line == "END_OF_TEXT":
        break
    lst += line.lower().split()
print(lst.count(W))
