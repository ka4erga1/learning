class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        s = s.split()
        for word in s:
            s1.append(word[::-1])
        s = " ".join(s1)
        return s
    
    print(reverseWords(1, "Let's take LeetCode contest"))