class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(i):
            res, cur = set(), {""}
            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    s, i = dfs(i + 1)
                    cur = {a + b for a in cur for b in s}
                elif expression[i] == ',':
                    res |= cur
                    cur ={""}
                    i += 1
                else:
                    cur = {x + expression[i] for x in cur}
                    i += 1
            res |= cur
            return res, i + 1
        return sorted(dfs(0)[0])
