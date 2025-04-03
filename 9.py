class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = 0
        char = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")
        s = s.replace("XC", "LXXXX")
        s = s.replace("XL", "XXXX")
        s = s.replace("CM","DCCCC")
        s = s.replace("CD","CCCC")
        for i in range(len(list(s))):
            b += char[list(s)[i]]
        return b
    romanToInt(1, "MCMXCIV")