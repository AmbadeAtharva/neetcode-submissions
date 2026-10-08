class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        sorted_numbers = sorted(d.keys(), key=d.get, reverse=True)
        
    
        return sorted_numbers[:k]