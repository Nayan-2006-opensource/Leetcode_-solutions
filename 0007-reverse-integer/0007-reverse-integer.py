class Solution:
    def reverse(self, x: int) -> int:
        num=x
        rev=0
        if num<0:
            num=num*(-1)
        while num>0:
            a=num%10
            rev=rev*10+a
            num=num//10

        if x<0:
            rev=rev*-1
        if rev<-2**31 or rev>2**31-1:
            rev=0
        return(rev)

        
        
        