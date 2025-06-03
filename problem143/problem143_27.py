input_int = input()
input_str = input()

K = int(input_int)
S = str(input_str)

if len(S)<=K:
    print(S)
elif len(S)>K:
    print(S[:K]+'...')