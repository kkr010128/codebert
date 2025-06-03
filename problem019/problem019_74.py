N_str, q_str = raw_input().split()
N = int(N_str)
q = int(q_str)
A =[]
B =[]
total =0

for i in range(N):
    t = raw_input().split()
    A.append([t[0],int(t[1])])

while A:
    name, time = A.pop(0)
    if time <= q:
        total += time
        B.append(name+" "+ str(total))
       
    else:
        time -= q
        total += q
        A.append([name, time])

print '\n'.join(B)