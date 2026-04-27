class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def sortthis(st):

            return "".join(sorted(list(st)))
        
        resdict={}
        for i in strs:
            if sortthis(i) not in resdict.keys():
                resdict[sortthis(i)]=[i]
            else:
                resdict[sortthis(i)]+=[i]
        
        return [i for i in resdict.values()]


        
 