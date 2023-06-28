# By self it run perfectly at other platform but here not

# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         pairs = []
#         totals = []

#         for list1 in sorted(nums1):
#             for list2  in sorted(nums2):
#                 pair = [list1, list2]
#                 total =  sum(pair)
#                 pairs.append(pair)
#                 totals.append(total)
            
#         sorted_pairs = [pair for _, pair in sorted(zip(totals, pairs))]
#         sorted_totals = sorted(totals)

#         for i in range(min(k, len(sorted_pairs))):
#             print(sorted_pairs[i])

# by chat gpt

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        pairs = []
        totals = []

        for num1 in sorted(nums1):
            for num2 in sorted(nums2):
                pair = [num1, num2]
                total = sum(pair)
                pairs.append(pair)
                totals.append(total)

        sorted_pairs = [pair for _, pair in sorted(zip(totals, pairs))]
        sorted_totals = sorted(totals)

        return sorted_pairs[:k]
