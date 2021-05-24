def maxarea(arr):
    stack=list()
    n=len(arr)
    ma=0
    i=0
    while i<n:
        if (not stack) or arr[stack[-1]]<=arr[i]:
            stack.append(i)
            i+=1
        else:
            ht=stack.pop()
            ar=arr[ht]*((i-stack[-1]-1) if stack else i)
            ma=max(ar,ma)
    while stack:
        ht=stack.pop()
        ar=arr[ht]*((i-stack[-1]-1) if stack else i)
        ma=max(ar,ma)
    return ma
a=list(map(int,input().split()))
print(maxarea(a))
