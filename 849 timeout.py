class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        c = []
        b = 0
        if seats.count(0) == 1:
            return 1
        elif seats.count(1) == 1:
            if seats.index(1) >= len(seats) // 2:
                return seats.index(1)
            else:
                return len(seats)-seats.index(1)-1
        for i in range(seats.count(1)):
            c.append(seats.index(1))
            seats.insert(seats.index(1),2)
            seats.remove(1)
        
        for i in range(len(c)-1):
            if abs(c[i] - c[i+1]) > b:
                b = abs(c[i] - c[i+1])
        if seats[0:c[0]].count(0) > b // 2 or seats[c[::-1][0]:].count(0)> b // 2:
            if seats[0:c[0]].count(0) > b // 2 and seats[0:c[0]].count(0) >= seats[c[::-1][0]:].count(0):
                b = seats[0:c[0]].count(0)
            if seats[c[::-1][0]:].count(0)> b // 2 and seats[0:c[0]].count(0) <= seats[c[::-1][0]:].count(0):
                b = seats[c[::-1][0]:].count(0)
            return b
        return b // 2 

    print(maxDistToClosest(1, [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
