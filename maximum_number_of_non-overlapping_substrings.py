class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        valid = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l
            ok = True
            while i <= r:
                c = s[i]
                if first[c] < l:
                    ok = False
                    break
                r = max(r, last[c])
                i += 1
            if ok:
                valid.append((l, r))
        valid.sort(key=lambda x: x[1])
        ans = []
        prev_end = -1
        for l, r in valid:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r
        return ans
