def main():
    S = input().rstrip()
    if S[-1] == "s":
        S = S + "es"
    else:
        S = S + "s"
    print(S)

main()
