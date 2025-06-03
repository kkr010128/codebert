def check(str):
    str2 = str[::-1]
    return str == str2



def main():
    s = input()
    n = len(s)
    first = s[:(n-1)//2]
    end = s[((n+3)//2)-1:]
    if all((check(s), check(first), check(end))):
        print("Yes")
    else:
        print("No")

main()