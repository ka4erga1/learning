class Solution(object):
    def productExceptSelf(self, nums):
        nums1 = []
        for i in nums:
            a = nums.index(i)
            nums.remove(i)
            b = 1
            for n in range(len(nums)):
                b *= nums[n]
            nums1.append(b)
            nums.insert(a, i)
        return nums1

    print(productExceptSelf(1, [-1,1,0,-3,3]))
