class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = []
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            else:
                hashset.append(nums[i])
        return False           
        
        