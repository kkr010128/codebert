arr = [[[0 for i1 in range(10)] for i2 in range(3)] for i3 in range(4)]

count=input()
for l in range(int(count)):
    b,f,r,v=input().split()
    arr[int(b)-1][int(f)-1][int(r)-1]+=int(v)

first_b = arr[0]
second_b = arr[1]
third_b = arr[2]
fourth_b= arr[3]

for m in range(3):
    for n in range(10):
        print(" "+str(first_b[m][n]),end="")
    print()
print("#"*20)
for m in range(3):
    for n in range(10):
        print(" "+str(second_b[m][n]),end="")
    print()
print("#"*20)
for m in range(3):
    for n in range(10):
        print(" "+str(third_b[m][n]),end="")
    print()
print("#"*20)
for m in range(3):
    for n in range(10):
        print(" "+str(fourth_b[m][n]),end="")
    print()