import math
N,M=map(int,input().split())
perfectSquare=N*M
X=math.sqrt(perfectSquare)
if(X==N and X==M):
    print("yes")
else:
    print("no")
