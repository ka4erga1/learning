class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = []
        result = "".join(dict.fromkeys(chars))
        result = list(result) 
        for char in result:
            if chars.count(char) == 1:
                s.append(char)
            elif chars.count(char) >= 10:
                s.append(char)
                s += "".join(list(str(chars.count(char))))
            else:
                s.append(char)
                s.append(str(chars.count(char)))
        chars = s
        print(chars)
        return len(chars)
    
    
    print(compress(1, ["a","a","b","b","c","c","c"]))