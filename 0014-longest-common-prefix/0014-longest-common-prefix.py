class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        len_pref = len(pref)
        for s in strs[1:]:
            while pref != s[0:len_pref]:
                len_pref -= 1
                if len_pref == 0:
                    return ""
                pref = pref[0:len_pref]
        return pref

        
        