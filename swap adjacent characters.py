N=int(input())
li=[int(m) for m in input().split()]
Q=0
if(len(li)==N):
    for i in range (0,N-1,2):
        Q=li[i+1]
        li[i+1]=li[i]
        li[i]=Q
    for i in range(N):
        print (li[i], end=" ")
