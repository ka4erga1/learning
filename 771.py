class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        b = list(jewels)
        c = 0
        for i in range(len(b)):
            c += stones.count(b[i])
        return c
    
    print(numJewelsInStones(1, "aA", "aAAbbbb"))