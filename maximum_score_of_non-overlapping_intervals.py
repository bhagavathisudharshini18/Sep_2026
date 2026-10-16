class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in a]
        n = len(a)
        dp = {}
        def solve(i, k):
            if i == n or k == 0:
                return(0, ())
            if (i, k) in dp:
                return dp[i, k]
            skip = solve(i + 1, k)
            j = bisect_right(starts, a[i][1])
            score, ids = solve(j, k - 1)
            take = (score + a[i][2], tuple(sorted(ids + (a[i][3],))))
            dp[i, k] = max(skip, take, key=lambda x: (x[0], tuple(-y for y in x[1])))
            return dp[i, k]
        return list(solve(0, 4)[1])
