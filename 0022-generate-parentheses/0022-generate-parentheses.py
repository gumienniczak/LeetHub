class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(cur, left_count, right_count):
            if len(cur) == 2 * n:
                ans.append("".join(cur))
                return
            if left_count < n:
                cur.append('(')
                generate(cur, left_count+1, right_count)
                cur.pop()
            
            if right_count < left_count:
                cur.append(')')
                generate(cur, left_count, right_count+1)
                cur.pop()
            
        generate([], 0, 0)
        return ans
            
            