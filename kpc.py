"""
1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
2. The following list is the key to characters map :
    0 -> .;
    1 -> abc
    2 -> def
    3 -> ghi
    4 -> jkl
    5 -> mno
    6 -> pqrs
    7 -> tu
    8 -> vwx
    9 -> yz
3. Complete the body of getKPC function - without changing signature - to get the list of all words that could be produced by the keys in str.
Use sample input and output to take idea about output.
Sample Input
78
Sample Output
[tv, tw, tx, uv, uw, ux]
"""


d={0:".;",1:"abc",2:"def",3:"ghi",4:"jkl",5:"mno",6:"pqrs",7:"tu",8:"vwx",9:"yz"}
s=input()
a=[]
def pair(a,l):
    temp=[]
    if a==[]:
        for j in l:
            a.append(j)
    else:
        for i in a:
            for j in l:
                temp.append(str(i)+str(j))
        a=temp
    
    return a
for i in s:
    a=pair(a,list(d[int(i)]))
print("[",end="")
print(*a,sep=",",end="")
print("]")
