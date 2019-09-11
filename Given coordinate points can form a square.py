X1,Y1=map(int,input().split())
X2,Y2=map(int,input().split())
X3,Y3=map(int,input().split())
X4,Y4=map(int,input().split())
if (Y2-Y1==X3-X2==Y3-Y4==X4-X1):
    print ("yes")
else:
    print ("no")
