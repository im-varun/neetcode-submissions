class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            diff = stones.pop() - stones.pop()
            if diff > 0:
                stones.append(diff)

        return 0 if len(stones) == 0 else stones[0]