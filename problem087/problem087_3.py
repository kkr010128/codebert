n = input()

mod = 0
for i in range(len(n)):
    mod += int(n[i])
    mod %= 9

print("Yes") if mod == 0 else print("No")