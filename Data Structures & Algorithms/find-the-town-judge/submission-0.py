class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {}
        outgoing = {}

        for pair in trust:
            a, b = pair[0], pair[1]
            outgoing[a] = outgoing.get(a, 0) + 1
            incoming[b] = incoming.get(b, 0) + 1

        for i in range(1, n + 1):
            if outgoing.get(i, 0) == 0 and incoming.get(i, 0) == n - 1:
                return i

        return -1