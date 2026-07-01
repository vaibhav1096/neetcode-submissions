class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset=collections.defaultdict(list)
        for s in strs:
            key=[0]*26
            for c in s:
                ind=ord(c)-ord('a')
                key[ind]+=1
            final_key= tuple(key)   
            # if final_key in hashset:
            hashset[final_key].append(s)
            # else:
            #     hashset[final_key]=[s]
        

        return list(hashset.values())
            



        