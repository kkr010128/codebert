n = int(input())
s = str(input())
ok = "Yes"
if n == 1:
    ok = "No"
if n % 2 == 1:
    ok = "No"
for i in range (0, n//2):
    if s[i] != s[i + n // 2] :
        ok = "No" 
print(ok)