class Solution(object):
    def findAnagrams(self, s, p):
        d1={}
        for i in p:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        left=0
        ans=[]
        d2={}
        k=len(p)
        for i in range(len(s)):
            d2[s[i]]=d2.get(s[i],0)+1
            if i >=len(p)-1:
                if d1==d2:
                    ans.append(left)
                d2[s[left]] -=1
                if d2[s[left]]==0:
                    d2.pop(s[left])
                left +=1
        return ans                



        
        