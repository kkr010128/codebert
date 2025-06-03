# Take both input K & S, then compare the length of S with K and assign it to length
# If the length is <= K print all
# And if length is >K print some of the character

K = int(input())
S = input()

x = 0

length = len(S)

if length <= K:
    print(S)
else:
    while x < K:
        print(S[x], end=(""))
        x += 1
    print("...")