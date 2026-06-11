class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        MOD = 10 ** 9 + 7
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([1])
        seen = set([1])
        distance = -1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neig in graph[curr]:
                    if neig not in seen:
                        queue.append(neig)
                        seen.add(neig)
            distance += 1
        
        return pow(2, distance - 1, MOD)
