s = input()
n = len(s)
def palindrome(s):
    ret = True
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            ret = False
            break
    return ret

check_1 = palindrome(s)
check_2 = palindrome(s[:(n)//2])
check_3 = palindrome(s[(n+2)//2:])

if check_1 and check_2 and check_3:
    print('Yes')
else:
    print('No')