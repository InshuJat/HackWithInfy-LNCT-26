class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        

        
        farthest = 0
        last_index = len(nums) - 1
        
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last_index:
                return True
                
        return farthest >= last_index