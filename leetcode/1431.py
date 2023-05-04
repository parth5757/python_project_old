# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """


#         nums.sort()
#         closest_sum = float('inf')
#         for i in range(len(nums) - 2):
#             left = i + 1
#             right = len(nums) - 1
        
#         while left < right:
#             curr_sum = nums[i] + nums[left] + nums[right]
#             if abs(target - curr_sum) < abs(target - closest_sum):
#                 closest_sum = curr_sum
            
#             if curr_sum == target:
#                 return curr_sum
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 right -= 1    
#         return closest_sum
# # p = Solution()
# # n = [1,1,1,0]
# # t = -100
# # print(p.threeSumClosest(n, t))
