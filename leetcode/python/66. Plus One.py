class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Convert each element in the list to an integer
        lst = [int(i) for i in digits]
        
        # Convert the list of integers to a single integer
        num = int(''.join(map(str, lst)))
        
        # Add 1 to the integer
        num += 1
        
        # Convert the result back to a list of integers
        res = [int(x) for x in str(num)]
        
        return res
p = Solution()
d = [9]
q = p.plusOne(d)
print(q)
