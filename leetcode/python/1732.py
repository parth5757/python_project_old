class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        r = 0
        gain = [0]+gain
        for i in range(1, len(gain)):
            gain[i] = gain[i-1] + gain[i]
            r = max(r, gain[i])
        return r
