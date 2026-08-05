class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            # graph[v].append(u)

        seen = set([k])
        stack = [k]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        
        for node in range(n):
            for neighbor in graph[node]:
                if neighbor in seen and node not in seen:
                    return [i for i in range(n)]
        return [node for node in range(n) if node not in seen]