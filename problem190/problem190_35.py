def is_palindrome(text):
    l = len(text)
    for i in range(l // 2 if l % 2 == 0 else (l + 1) // 2):
        if text[i] != text[l - 1 - i]:
            return False
    return True

s = input()
q1 = is_palindrome(text=s)
q2 = is_palindrome(text=s[0:(len(s) - 1) // 2])
q3 = is_palindrome(text=s[(len(s) + 3) // 2 - 1:len(s)])
print("Yes" if q1 and q2 and q3 else "No")