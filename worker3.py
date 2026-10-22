class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        numMap = {}
        n = len(nums)

        for num in nums:
            if num in numMap:   
                numMap[num] += 1
            else:
                numMap[num] = 1
        
        for key , val in numMap.items():
            if (val > n//2):
                ans = key
        return ans