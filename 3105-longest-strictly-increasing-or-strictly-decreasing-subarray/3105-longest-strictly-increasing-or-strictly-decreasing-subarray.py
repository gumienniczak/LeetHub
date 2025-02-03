class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        scores_inc = []
        scores_dec = []
        if not nums:
            score_inc = 0
            score_dec = 0
            scores_inc.append(0)
            scores_dec.append(0)
        else:
            score_inc = 1
            score_dec = 1
            scores_inc.append(1)
            scores_dec.append(1)
        for i in range(len(nums) - 1):
            current_number = nums[i]
            next_number = nums[i + 1]
            if next_number > current_number:
                score_inc += 1
            elif next_number < current_number:
                score_dec += 1
            else:
                scores_inc.append(score_inc)
                scores_dec.append(score_dec)
                score_inc = 1
                score_dec = 1
            scores_inc.append(score_inc)
            scores_dec.append(score_dec)
        return max((max(scores_inc), max(scores_dec)))
