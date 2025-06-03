def main():
    k = int(input())
    s = input()
    s_len = len(s)
    
    if s_len <= k:
        print(s)
    else:
        s = s[0:k] + '...'
        print(s)
    
main()