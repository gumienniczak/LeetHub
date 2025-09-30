class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numbers = []
        ops = set(["+", "-", "*", "/"])
        for el in tokens:
            if el in ops:
                two = numbers.pop()
                one = numbers.pop()
                if el == "+":
                    numbers.append(one + two)
                elif el == "-":
                    numbers.append(one - two)
                elif el == "*":
                    numbers.append(one * two)
                else:
                    division = (float(one) / float(two))
                    numbers.append(int(division))
            else:
                numbers.append(int(el))

        return numbers[0]