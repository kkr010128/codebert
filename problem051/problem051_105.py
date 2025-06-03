while True:
    a = input()
    b = a.split(' ')
    H = int(b[0])
    W = int(b[1])
    if H == 0 and W == 0:
        break
    elif H % 2 == 0:
        for i in range(H//2):
            if W % 2 == 0:
                print('#.'*int(W//2))
                print('.#'*int(W//2))
            elif W % 2 == 1:
                print('#.'*int((W-1)//2)+'#')
                print('.#'*int((W-1)//2)+'.')
    elif H % 2 == 1:
        for e in range((H-1)//2):
            if W % 2 == 0:
                print('#.'*int(W//2))
                print('.#'*int(W//2))
            elif W % 2 == 1:
                print('#.'*int((W-1)//2)+'#')
                print('.#'*int((W-1)//2)+'.')
        if W % 2 == 0:
            print('#.'*int(W//2))
        elif W % 2 == 1:
            print('#.'*int((W-1)//2)+'#')
    print()