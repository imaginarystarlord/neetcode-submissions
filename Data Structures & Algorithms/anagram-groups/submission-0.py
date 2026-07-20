class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for word in strs:
            newStr = "".join(sorted(word))
            if newStr in myDict:
                myDict[newStr].append(word)
            else:
                myDict[newStr] = [word]

        return list(myDict.values())
        