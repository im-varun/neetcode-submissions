class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        sq_sum = n
        while sq_sum != 1:
            sq_sum = sum(int(c)**2 for c in str(sq_sum))
            if sq_sum in hashset:
                return False

            hashset.add(sq_sum)

        return True