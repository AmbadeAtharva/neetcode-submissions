class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            asc_count = [0]*26
            for i in s:
                asc_count[ord(i) - ord('a')] += 1
            res[tuple(asc_count)].append(s)
        return list(res.values())


