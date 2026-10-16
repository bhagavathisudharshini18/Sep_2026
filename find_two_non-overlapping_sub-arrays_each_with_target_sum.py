class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * (n + 1)
        left = 0
        curr_sum = 0
        ans = INF
        for right in range(n):
            curr_sum += arr[right]
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == target:
                length = right - left + 1
                if best[left] != INF:
                    ans = min(ans, length + best[left])
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]
        return -1 if ans == INF else ans
