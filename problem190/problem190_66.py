s=input()
n=len(s)
s1=s[:(n-1)//2]
s2=s[n+3//2:]
def ispalindrome(str):
    if str==str[::-1]:
        s1=s[:(n-1)//2]
        if s1==s1[::-1]:
            s2=s[n+3//2:]
            if s2==s2[::-1]:
                return 'Yes'
            return 'No'
        return 'No'
    else:
        return 'No'
print(ispalindrome(s))