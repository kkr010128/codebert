in_string = input()
in_arr = in_string.split()
N = int(in_arr[0])
A = int(in_arr[1])
B = int(in_arr[2])

if ((B-A) % 2) == 0:
    print(int((B-A)//2))
else:
    if (N-B) > A-1:
        print(int(A+(B-A-1)//2))
    else:
        print(int(N-B+1+((N-(A+N-B+1))//2)))
