class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sr = sc = 0
        litter_id = [[-1] * n for _ in range(m)]
        litter_count = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1
        full_mask  = (1 << litter_count) - 1
        if full_mask == 0:
            return 0
        best = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((sr, sc, 0, energy))
        best[sr][sc][0] = energy
        directions = [(1, 0), (-1, 0),(0, 1),(0, -1)]
        moves = 0
        while q:
            for _ in range(len(q)):
                r, c, mask, remaining = q.popleft()
                if mask == full_mask:
                    return moves
                if remaining == 0:
                    continue
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    new_energy = remaining - 1
                    new_mask = mask
                    if classroom[nr][nc] == 'L':
                        new_mask |= 1 << litter_id[nr][nc]
                    if classroom[nr][nc] == 'R':
                        new_energy = energy
                    if best[nr][nc][new_mask] >= new_energy:
                        continue
                    best[nr][nc][new_mask] = new_energy
                    q.append((nr, nc, new_mask, new_energy))
            moves += 1
        return -1
