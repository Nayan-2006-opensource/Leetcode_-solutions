class Solution:
    def reverse(self, x: int) -> int:
        n=x
        rev=0
        if x<0:
            n=n*-1
        while n>0:
            a=n%10
            rev=rev*10+a
            n=n//10
        if x<0:
            rev=rev*-1
        if rev<-2**31 or rev>2**31-1:
            rev=0
        return rev




        
        
        