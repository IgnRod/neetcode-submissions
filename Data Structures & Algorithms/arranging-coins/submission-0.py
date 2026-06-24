class Solution:
    def arrangeCoins(self, n: int) -> int:
        level = 0
        while(n > 0):
            if(n - (level+1) < 0):
                break
            level = level + 1
            n = n - level
            print(level)
        return level