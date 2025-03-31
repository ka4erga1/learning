class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1 = []
        for i in nums:
            b = nums.index(i)
            if target < 0:
                nums.insert(b, target-1)
            else:
                nums.insert(b, target+1)
            nums.remove(i)
            try:
                num1.append(nums.index(target - i))
                num1.insert(0, b)
                break
            except ValueError:
                continue
        return num1


    print(twoSum(1, [-1,-2,-3,-4,-5], -8))