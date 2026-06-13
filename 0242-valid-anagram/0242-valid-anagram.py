class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_1 ={}
        hash_map_2 = {}
        for i in s:
            if i in hash_map_1:
                hash_map_1[i] += 1
            else:
                hash_map_1[i] = 1
        for j in t:
            if j in hash_map_2:
                hash_map_2[j] += 1
            else:
                hash_map_2[j] = 1
        
        return hash_map_1 == hash_map_2