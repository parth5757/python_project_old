class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def canSegment(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet and canSegment(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return canSegment(0)

# # Example usage:
# sol = Solution()
# s1, wordDict1 = "leetcode", ["leet", "code"]
# print(sol.wordBreak(s1, wordDict1))  # Output: True

# s2, wordDict2 = "applepenapple", ["apple", "pen"]
# print(sol.wordBreak(s2, wordDict2))  # Output: True

# s3, wordDict3 = "catsandog", ["cats", "dog", "sand", "and", "cat"]
# print(sol.wordBreak(s3, wordDict3))  # Output: False
