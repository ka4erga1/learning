class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        start, end = 0, 0
        while start < len(nums) and end < len(nums):
            if end < len(nums)-1:
                if (nums[end] + 1) == nums[end + 1]:
                    end += 1
                elif nums[start] == nums[end]:
                        result.append(str(nums[start]))
                        end = end + 1
                        start = end
                else:
                    result.append(str(nums[start]) + "->" + str(nums[end]))
                    end = end + 1
                    start = end
            else:
                if nums[start] == nums[end]:
                        result.append(str(nums[start]))
                        start += 1
                        end += 1
                else:
                    result.append(str(nums[start]) + "->" + str(nums[end]))
                    end = end + 1
                    start = end
            
        return result
    
    print(summaryRanges(1, [0,2,3,4,6,8,9]))