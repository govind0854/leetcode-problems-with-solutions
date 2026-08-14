class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        k = len(s1)
        left = 0

        d = {}
        for ch in s1:
            d[ch] = d.get(ch, 0) + 1

        d1 = {}
        for i in range(k):
            d1[s2[i]] = d1.get(s2[i], 0) + 1

        if d == d1:
            return True

        for i in range(k, len(s2)):

            d1[s2[i]] = d1.get(s2[i], 0) + 1

            d1[s2[left]] -= 1

            if d1[s2[left]] == 0:
                d1.pop(s2[left])

            left += 1

            if d == d1:
                return True

        return False