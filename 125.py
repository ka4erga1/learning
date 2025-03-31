class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(list(s)) == 1:
            return True
        else:
            s = str(s)
            s = "".join(filter(str.isalnum, s))
            s = s.lower()
            if s == s[::-1]:
                return True
            else:
                return False


    print(isPalindrome(1, "A man, a plan, a canal: Panama"))