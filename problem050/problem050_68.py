ans = []
add = ans.append
for line in open(0).readlines():
    H, W = map(int, line.split())
    if not H:
        break
    r = "#"*W+"\n"
    add(r)
    add(("#"+"."*(W-2)+"#\n")*(H-2))
    add(r)
    add("\n")
open(1, 'w').writelines(ans)

