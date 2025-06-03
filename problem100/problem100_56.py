x = int(input())

def check(input):
    one = 1800
    two = 1999
    kyu = 1
    while one >= 400:
        if one <= input <= two:
            return kyu
        kyu += 1
        one -= 200
        two -= 200

print(check(x))
