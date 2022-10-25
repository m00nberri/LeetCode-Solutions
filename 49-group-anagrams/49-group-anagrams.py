class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = []
        output = []
        counter = 0
        
        for s in strs:
            cmap = {}
            for c in s:
                if c in cmap:
                    cmap[c] += 1
                else:
                    cmap[c] = 1
            
            if cmap in anagrams:
                output[anagrams.index(cmap)].append(s)
            else:
                anagrams.append(cmap)
                output.append([s])
                
        return output