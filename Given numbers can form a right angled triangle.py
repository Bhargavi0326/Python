A,B,C=map(int,input().split())
if (A <= 100000 and B <= 100000 and C <= 100000):
    if(A+B>=C or B+C>=A or C+A>=B and (A**2)+(B**2)==(C**2)):
       print ("yes")

