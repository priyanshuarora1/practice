"""
1 						1 	
1 	2 				2 	1 	
1 	2 	3 		3 	2 	1 	
1 	2 	3 	4 	3 	2 	1 
"""

n=int(input())
sp=2*n-3
vs=1
ve=0
for i in range(1,n+1):
    vs=1
    for _ in range(i):
        print(vs,"\t",end="")
        vs+=1
    print("\t"*sp,end="")
    sp-=2
    ve=vs-1
    if ve==n:
        ve-=1
        sl=i-1
    else:
        sl=i
    
    for _ in range(sl):
        print(ve,"\t",end="")
        ve-=1
    print()
