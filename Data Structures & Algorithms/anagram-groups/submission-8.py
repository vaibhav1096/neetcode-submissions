class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictn=collections.defaultdict(list)

        for n in strs:
            key=[0]*26

            for c in n:
                key_=ord(c)-ord("a")
                key[key_]+=1
            dictn[tuple(key)].append(n)
        
        return list(dictn.values())
        