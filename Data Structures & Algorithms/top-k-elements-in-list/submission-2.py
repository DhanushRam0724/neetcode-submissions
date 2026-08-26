class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        ans = [[] for _ in range(len(nums) + 1)]
        for value, freq in freqs.items():
            ans[freq].append(value)

        final_ans = []
        count = 0

        for i in range(len(nums), -1, -1):
            if ans[i] != []:
                final_ans.extend(ans[i])
            if len(final_ans) >= k:
                return final_ans[:k]