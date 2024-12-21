# 217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```
Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```
Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 ```

Constraints:

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

Notes:

Brute force: 
- go through each and every element by using two loops - check each pair 

hashset:
- create a hashset of nums, check if len(hashset_nums)==len(nums) 

sorting:
- sort nums
- in range(1,len(nums)) #ensuring it does not go out of bound
- if nums[i] == nums[i-1]