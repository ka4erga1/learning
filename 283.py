class Solution(object):
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        """
        num = nums.count(0)
        for i in range(num):
            nums.remove(0)
            nums.append(0)
            if sum(nums[((len(nums)) - num):len(nums)])/1 == 0:
                break
        return nums
    print(moveZeroes(1, [0,1,0,3,12]))