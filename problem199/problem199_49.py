s = input()
ans = "No"

for i in range(1, 6):
    if s == "hi" * i:
        ans = "Yes"

print(ans)