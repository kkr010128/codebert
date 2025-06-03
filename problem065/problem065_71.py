W = input().lower()
count = 0
while True:
    a = input()
    if a == "END_OF_TEXT":
        break
    a = a.lower()
    a = a.split()
    for i in range(len(a)):
        if W == a[i]:
            count += 1          
print(count)   