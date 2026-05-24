from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dc = Counter(nums)

        arr = []
        for i, j in dc.items():
            arr.append([j, i])
        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])
        return ans
