"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""
def dtob(num):
    i=0
    ans=0
    while(num!=0):
        r=(num%2)
        num=num//2
        ans+=r*(10**i)
        i+=1
    return ans
def btod(num):
    i=0
    ans=0
    while(num!=0):
        r=(num%10)
        num=num//10
        ans+=r*(2**i)
        i+=1
    return ans


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a)
        b=int(b)
        a1=btod(a)
        b1=btod(b)
        c=a1+b1
        c=(dtob(c))
        return str(c)
