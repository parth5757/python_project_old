108. Convert Sorted Array to Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(left, right):
            if left > right:
                return None

            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root

        return buildBST(0, len(nums) - 1)

# Example usage:
sol = Solution()
nums1 = [-10, -3, 0, 5, 9]
root1 = sol.sortedArrayToBST(nums1)
# Print the BST using inorder traversal to check if it's balanced
def inorderTraversal(node):
    if not node:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

print(inorderTraversal(root1))  # Output: [-10, -3, 0, 5, 9]
