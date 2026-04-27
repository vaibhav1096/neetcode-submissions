class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # def sortthis(st):

        #     return "".join(sorted(list(st)))
        
        # resdict={}
        # for i in strs:
        #     if sortthis(i) not in resdict.keys():
        #         resdict[sortthis(i)]=[i]
        #     else:
        #         resdict[sortthis(i)]+=[i]
        
        # return [i for i in resdict.values()]
        resdict={}
        for string in strs:
            code=[0]*26
            for i in string:
                code[ord(i)-ord('a')]+=1
            key=str(code) 
            if key in resdict:
                resdict[key] += [string]
            else:
                resdict[key]=[string]
        
        return [i for i in resdict.values()]




        
 