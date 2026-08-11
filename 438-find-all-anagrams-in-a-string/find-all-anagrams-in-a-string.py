class Solution(object):
    def findAnagrams(self, s, p):
        # d={}
        # for i in s:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # c={}
        # for i in p:
        #     if i in c:
        #         c[i]+=1
        #     else:
        #         c[i]=1
        # for i in range(len(p)):
        #     if d[i] in c[i]:
        #         d[i]+=1
        #     else:
        #         d[i]-=1
        # for i in range(len(p),len(s)):
        #     if d[i] in c[i]:
        #         d[i]+=1
        #     else:
        #         d[i]-=1

        d={}
        for i in p:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        left=0
        d1={}
        ans=[]
        k=len(p)
        for i in range(len(s)):
            d1[s[i]]=d1.get(s[i],0)+1
            if i >= len(p)-1:
                if d1==d:
                    ans.append(left)
                d1[s[left]] -= 1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left +=1
        return ans



           
               
        



        

        
        