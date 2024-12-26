#Brute force: O(N^2), O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)+1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
            return False    
        

#hashset length: O(N), O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            hashset.add(num) 
        return len(hashset) != len(nums)
    
#hashset: O(N), O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num) 
        return False  