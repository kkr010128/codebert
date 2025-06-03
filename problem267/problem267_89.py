def is_passcode_exist(S,passcode):
    passcode_idx = 0
    passcode_is_exist = False
    for c in S:
        if passcode_idx == 3:
            passcode_is_exist = True
            break
        if passcode[passcode_idx] == c:
            passcode_idx += 1
    if passcode_idx == 3:
        passcode_is_exist = True
    return passcode_is_exist

if __name__ == "__main__":
    N = int(input())
    S = input()
    count = 0
    for i in range(0,1000):
        if is_passcode_exist(S,str(i).zfill(3)):
            count += 1
    print(count)