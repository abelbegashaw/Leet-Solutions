class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        result = []

        segments = []
        lb = rb = 0
        while lb < n:
            left, right = rb + 1, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] - nums[rb] <= maxDiff:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if right == rb:
                segments.append([lb, rb])
                lb = rb = rb + 1
            else:
                rb = right

        def find(node):
            left, right = 0, len(segments) - 1
            while left <= right:
                mid = (left + right) // 2
                if segments[mid][0] <= node <= segments[mid][1]:
                    return mid
                elif segments[mid][0] <= node:
                    left = mid + 1
                else:
                    right = mid - 1
            

        print(segments)
        for u, v in queries:
            result.append(find(u) == find(v)) 

        return result
            

