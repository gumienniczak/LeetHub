class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        N1 = len(word1)
        N2 = len(word2)

        def alternate(str1, str2):
            output = ""
            for a, b in zip(str1, str2):
                output += a
                output += b
            return output

        if N1 != N2:
            if N1 > N2:
                output = alternate(word1[:N2], word2)
                output += word1[N2:]
            else:
                output = alternate(word1, word2[:N1])
                output += word2[N1:]
        else:
            output = alternate(word1, word2)
        
        return output