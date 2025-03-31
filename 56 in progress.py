class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        intervals1 = []
        if len(intervals) == 1:
            return(intervals)
        while i != len(intervals):
            if i == len(intervals) - 1:
                if intervals[i][1] == intervals1[len(intervals1) - 1][1]:
                    break
                else:
                    intervals1.append(intervals[i])
                    break
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals1.append([intervals[i][0],intervals[i + 1][1]])
                i += 2
            else:
                intervals1.append(intervals[i])
                i += 1
        return intervals1

    print(merge(1, [[1,4],[0,4]])) ## doljen 0, 4