class Solution(object):
    def isPalindrome(self, head):
        if head == head[::-1]:
            return True
        else:
            return False
    print(isPalindrome(1, [1,2,2]))