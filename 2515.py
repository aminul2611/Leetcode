class Solution: 
    def closetTargetDistance(self, words, target, startIndex):
        n = len(words)
       
        if target not in words:
            return -1
        
        ans = float('inf')
       
        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                dist = min(diff, n - diff)
                ans = min (ans, dist)
        return ans
    