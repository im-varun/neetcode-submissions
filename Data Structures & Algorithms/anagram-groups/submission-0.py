class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            count_tuple = tuple(count)
            if count_tuple in hashmap:
                hashmap[count_tuple].append(s)
            else:
                hashmap[count_tuple] = [s]

        output = list(hashmap.values())

        return output
