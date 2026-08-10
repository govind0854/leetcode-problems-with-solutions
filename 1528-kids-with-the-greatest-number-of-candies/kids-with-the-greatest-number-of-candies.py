class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        r=[]
        m=0 
        for i in candies :
            if i > m:
                m=i
        for i in candies:
            if i+extraCandies >= m:
                r.append(True)
            else:
                r.append(False)
        return r

        
        