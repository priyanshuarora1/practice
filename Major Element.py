def major(arr):
    element=arr[0]
    ctr=1
    n=len(arr)
    for i in range(1,n):
        if arr[i]==element:
            ctr+=1
        else:
            ctr-=1
        if ctr==0:
            element=arr[i]
            ctr+=1
    ctr=0
    for i in arr:
        if i==element:
            ctr+=1
    if ctr>n//2:
        print(element)
    else:
        print("No Solution")
        
a=list(map(int,input().split()))
major(a)
