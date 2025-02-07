class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        # we use a manual index counter instead of range so that we can modify it while running the function
        i = 0 
        while i < len(s):
            if i < len(s) - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
                output += (roman_to_int_map[s[i + 1]] - roman_to_int_map[s[i]])
                i += 2
            else:
                output += roman_to_int_map[s[i]]
                i += 1

        return output