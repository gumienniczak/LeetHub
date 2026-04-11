class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(cur, left_count, right_count):
            if len(cur) == 2 * n:
                ans.append(cur)
                return
            if left_count < n:
                cur += "("
                generate(cur, left_count+1, right_count)
                cur = cur[:-1]
            
            if right_count < left_count:
                cur += ")"
                generate(cur, left_count, right_count+1)
                cur = cur[:-1]
            
        generate("", 0, 0)
        return ans
            
            