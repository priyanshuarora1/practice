"""
1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
3. Complete the body of getStairPaths function - without changing signature - to get the list of all paths that can be used to climb the staircase up.

Sample Input
3
Sample Output
[111, 12, 21, 3]
"""

n=int(input())
def stair(n):
    if n==0:
        bres=[]
        bres.append("")
        return bres
    elif n<0:
        bres=[]
        return bres
    path1=stair(n-1)
    path2=stair(n-2)
    path3=stair(n-3)
    path=[]
    for i in path1:
        path.append("1"+i)
    for i in path2:
        path.append("2"+i)
    for i in path3:
        path.append("3"+i)
    return path
print("[",end="")
print(*stair(n),sep=", ",end="")
print("]")
