class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if num<0:
            num=num*(-1)
        while num>0:
            a=num%10
            rev=rev*10+a
            num=num//10
        if x==rev:
            return True
        else:
            return False


        