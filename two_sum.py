class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict  =  {}
        for i in range(nums):
            
            residual =  target -  nums[i]
            if residual in nums_dict:
                return i, nums_dict{i}
            else:
                nums_dict{nums[i]} =  i
