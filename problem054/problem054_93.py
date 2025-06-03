a = {}
for s in ["S", "H", "C", "D"]:
    a.update({f'{s} {i}': 0 for i in range(1, 14)})
n = int(input())
for _ in range(n):
    s = input()
    del a[s]
        
a = list(a)
for i in range(len(a)):
    print(a[i])
    

    
    
