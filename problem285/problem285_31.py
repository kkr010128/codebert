def main():
    s = input()
    arr = [0]*(len(s)+1)
    for i in range(len(s)):
        c = s[i]
        if c == "<":
            arr[i+1] = arr[i]+1
    for i in reversed(range(len(s))):
        c = s[i]
        if c == ">":
            arr[i] = max(arr[i], arr[i+1]+1)
    print(sum(arr))

if __name__ == "__main__":
    main()
