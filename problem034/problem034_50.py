def right(a,b,a1,a2,a3,a4,a5,a6):
    b1=a6
    b2=a5
    b3=a4
    b4=a3
    b5=a2
    b6=a1
  
    if a>b:
        tmp_a=a
        a=b
        b=tmp_a
        
    if [a,b]==[a1,a2]:
        right_side=[a3,b3]
    elif [a,b]==[a1,a3]:
        right_side=[a5,b5]
    elif [a,b]==[a1,a4]:
        right_side=[a2,b2]
    elif [a,b]==[a1, a5]:
        right_side=[a4,b4]
    elif [a,b]==[a2, a3]:
        right_side=[a1,b1]
    elif [a, b]==[a2, a4]:
        right_side=[a6,b6]
    elif [a,b]==[a2,a6]:
        right_side=[a3,b3]
    elif [a,b]==[a3, a5]:
        right_side=[a1,b1]
    elif [a,b]==[a3, a6]:
        right_side=[a5,b5]
    elif [a, b]==[a4, a5]:
        right_side=[a6,b6]
    elif [a,b]==[a4,a6]:
        right_side=[a2,b2]
    elif [a,b]==[a5,a6]:
        right_side=[a4,b4]
  
    return right_side
    

initial=list( map(int,input().split()))
num_of_q=int(input())

for i in range(0, num_of_q):
    a=list(map(int, input().split()))
    flag=0
    if a[0]>a[1]:
        flag=1
    answer=right(*a,*initial)
    print(answer[flag])
    
    

