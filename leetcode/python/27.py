class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)
p = Solution()
n = [3,2,2,3]
t = 3
print(p.removeElement(n, t))
