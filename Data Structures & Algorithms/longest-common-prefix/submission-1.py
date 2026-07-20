class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        pre = ""
        for i in range(len(first)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or first[i] != strs[j][i]:
                    return pre
            pre += first[i]
        
        return pre