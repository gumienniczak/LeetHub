class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(cur, left_count, right_count):
            if len(cur) == 2 * n:
                ans.append(cur)
                return
            if left_count < n:
                generate(cur + "(", left_count+1, right_count)
            
            if right_count < left_count:
                generate(cur + ")", left_count, right_count+1)
            
        generate("", 0, 0)
        return ans
            
            