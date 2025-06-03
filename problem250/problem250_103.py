x = int(input())
ans = "No"
if x == 2:
    ans = "Yes"
while ans == "No":
    for i in range(2,max(x//2,3)):
        ans = "Yes"
        if x % i == 0:
            x += 1
            ans = "No"
            break
print(x)