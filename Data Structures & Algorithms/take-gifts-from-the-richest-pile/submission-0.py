class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()

        for i in range(k):
            max_gifts = gifts.pop()
            gifts.append(int(max_gifts ** 0.5))
            gifts.sort()

        output = sum(gifts)

        return output