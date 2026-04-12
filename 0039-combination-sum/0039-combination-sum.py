class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def generate(current: list, cur_sum: int, index: int):
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append(current[:])
            
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                current.append(candidate)
                cur_sum += candidate
                generate(current, cur_sum, i)
                current.pop()
                cur_sum -= candidate
            
        generate([], 0, 0)
        return ans