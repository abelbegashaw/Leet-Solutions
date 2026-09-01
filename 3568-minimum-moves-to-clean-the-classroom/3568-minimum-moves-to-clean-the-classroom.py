class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        # Pre - process
        m, n = len(classroom), len(classroom[0])
        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        sx, sy = -1, -1
        litters, identifier = {}, 0
        for i in range(len(classroom)):
            for j in range(len(classroom[0])):
                if classroom[i][j] == 'L':  
                    litters[(i, j)] = identifier
                    identifier += 1
                elif classroom[i][j] == 'S':
                    sx, sy = i, j
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # BFS part
        queue = deque([(sx, sy, energy, 0)])
        jump = 0
        best = [[[-1 for _ in range(1 << len(litters) )]  for _ in range(n)] for _ in range(m)]

        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y, power, mask = queue.popleft()
            
                if mask == (1 << len(litters)) - 1:
                    return jump

                for dx, dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if inbound(new_x, new_y) and classroom[new_x][new_y] != 'X' and power:
                        new_mask = mask | (1 << litters[(new_x, new_y)]) if (new_x, new_y) in litters else mask
                        new_power = energy if classroom[new_x][new_y] == 'R' else power - 1
                        if best[new_x][new_y][new_mask] < new_power:
                            best[new_x][new_y][new_mask] = new_power
                            queue.append([new_x, new_y, new_power, new_mask])
            
            jump += 1
        return -1