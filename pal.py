class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == head[::-1]:
            return True
        else:
            return False
    print(isPalindrome(1, [1,2,2]))