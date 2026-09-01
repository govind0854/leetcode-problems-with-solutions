class Solution(object):
    def maxFreqSum(self, s):
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        max_v=0
        max_c=0
        vowels="aeiou"
        for ch in d:
            if ch in vowels:
                max_v=max(max_v,d[ch])
            else:
                max_c=max(max_c,d[ch])
        return max_v+max_c
        