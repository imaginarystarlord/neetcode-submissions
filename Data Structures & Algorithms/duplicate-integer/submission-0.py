class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrayDict = {}
        for i in range(len(nums)):
            if nums[i] in arrayDict:
                return True
            else:
                arrayDict[nums[i]] = 1
        return False