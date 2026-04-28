class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for string in strs:
            encoded+=str(len(string))+"#"+string
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i < len(s):
            pointer=i
            while s[pointer]!="#" and pointer<len(s):
                pointer+=1
            integer=int(s[i:pointer])  
            decoded.append("".join(s[pointer+1:pointer+1+integer]))
            # print(decoded)
            i=pointer+integer+1
        
        return decoded


                



