N=int(input())
li=[int(m) for m in input().split()]
if(N<100000):
    if(N==len(li)):
        min=li.index(min(li))
        max=li.index(max(li))
        print((min+1),(max+1))
