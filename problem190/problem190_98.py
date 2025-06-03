s = input()
n = len(s)

def func():
    if n == 3 and s[0] == s[2]:
        return"Yes"
    else:
        a = 0
        for i in range(n//2):
            if s[i] == s[n - 1 - i]:
                a += 1
                if a == n//2:
                    b = 0
                    for j in range((n-1)//4):
                        if s[j] == s[(n-1)//2 - 1 - j]:
                            b += 1
                            if b == (n-1)//4:
                                c = 0
                                for k in range((n - (n+3)//2 + 1)//2):
                                    if s[(n+3)//2 - 1 + k] == s[n - 1 - k]:
                                        c += 1
                                        if c == (n - (n+3)//2 + 1)//2:
                                            return "Yes"
                        else:
                            return "No"
            else:
                return "No"
        
print(func())