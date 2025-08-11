class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        beg = 0
        end = len(s) - 1
        back_counter = 0
        for i in range(len(s)):
            if s[i] == " " or i == end:
                if i != end:
                    back_counter = i - 1
                else:
                    back_counter = i
                while back_counter >= beg:
                    output += s[back_counter]
                    back_counter -= 1
                if i != end:
                    output += " "
                beg = i + 1
 
        return output


