def main():
    x = int(input())
    for A in range(-118,120):
        for B in range(-119,119):
            if (A**5 - B**5) == x:
                return([A,B])

ans = main()
print(' '.join(str(n) for n in ans))
