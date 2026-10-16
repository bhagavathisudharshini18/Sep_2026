class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = [None] * (2 * n)
        def merge(a, b):
            p1, c1 = a
            p2, c2 = b
            c = c1[:]
            for r in range(k):
                c[p1 * r % k] += c2[r]
            return p1 * p2 % k, c
        for i, x in enumerate(nums):
            c = [0] * k
            c[x % k] = 1
            seg[n + i] = (x % k, c)
        for i in range(n - 1, 0, -1):
            seg[i] = merge(seg[i * 2], seg[i * 2 + 1])
        def update(i, x):
            i += n
            c = [0] * k
            c[x % k] = 1
            seg[i] = (x % k, c)
            while i > 1:
                i //= 2
                seg[i] = merge(seg[i * 2], seg[i * 2 + 1])
        def query(l, r):
            left = right = None
            l += n
            r += n
            while l < r:
                if l & 1:
                    left = seg[l] if left is None else merge(left, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    right = seg[r] if right is None else merge(seg[r], right)
                l //= 2
                r //= 2
            return merge(left, right) if left and right else left or right
        ans = []
        for i, v, start, x in queries:
            update(i, v)
            ans.append(query(start, n)[1][x])
        return ans 
