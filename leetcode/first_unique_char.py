class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        indices = {}

        for i, j in enumerate(s):
            if j not in indices:
                indices[j] = [i]
            else:
                indices[j].append(i)

        for i in s:
            if len(indices[i]) == 1:
                return indices[i][0]

        return -1
