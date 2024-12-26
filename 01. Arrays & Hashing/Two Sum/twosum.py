#brute force O(N^2), O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
#hashset O(N), O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashset:
                return [i,hashset[diff]]
            else:
                hashset[nums[i]] = i    


class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {} #val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashset:
                return[i, hashset[diff]]
            else:
                hashset[n] = i    