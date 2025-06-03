a,b=map(int,input().split())

def factorization(n):
    arr = []
    tmp = n

    for i in range(2, int(n**0.5//1)+1):
        if tmp%i==0:
            cnt = 0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            arr.append([i,cnt])
    if tmp!=1:
        arr.append([tmp,1])
    if arr==[]:
        arr.append([n,1])
    return arr

a_arr = factorization(a)
b_arr = factorization(b)
a_map = {str(arr[0]):arr[1] for arr in a_arr}
b_map = {str(arr[0]):arr[1] for arr in b_arr}

factor = set(list(a_map.keys())+list(b_map.keys()))
ans = 1
for i in factor:
  if str(i) in a_map.keys():
    a_num = a_map[str(i)]
  else:
    a_num = 0
    
  if str(i) in b_map.keys():
    b_num = b_map[str(i)]
  else:
    b_num = 0
  
  ans *= int(i)**(max(a_num,b_num))
print(ans)