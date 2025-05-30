# Last updated: 5/19/2025, 10:14:40 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0 
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        