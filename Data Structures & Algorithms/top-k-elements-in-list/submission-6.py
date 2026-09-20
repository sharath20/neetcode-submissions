class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        for i in nums:
            hash_map[i]  = 1 + hash_map.get(i,0)
        
        sorted_list = sorted(hash_map,key = hash_map.get,reverse=True)
        return sorted_list[:k]