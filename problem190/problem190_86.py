S = input()
lenS = len(S)
ans = "No"

def checkPalindrome(string):
    l = len(string)
    string2 = string[::-1]
    if string[:l//2] == string2[:l//2]:
        return True
    else:
        return False

if checkPalindrome(S):
    if checkPalindrome(S[:(lenS-1)//2]):
        if checkPalindrome(S[(lenS+3)//2-1:]):
            ans = "Yes"

print(ans)