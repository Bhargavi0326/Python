A,B,C=map(int,input().split())
if (A <= 100000 and B <= 100000 and C <= 100000):
    if(A!= B!=C and (A+B>=C or B+C>=A or C+A>=B)):
        print ("yes")
    else:
        print ("no")
