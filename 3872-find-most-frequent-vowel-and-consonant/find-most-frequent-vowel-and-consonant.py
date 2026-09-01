class Solution(object):
    def maxFreqSum(self, s):
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        max_vowels=0
        max_consonants=0
        vowels="aeiou"
        for i in d:
            if i in vowels:
                max_vowels=max(max_vowels,d[i])
            else:
                max_consonants=max(max_consonants,d[i])
        return max_vowels+max_consonants
        

        
        
        