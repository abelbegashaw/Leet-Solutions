class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        integers = defaultdict(list)
        for _ in range(len(nums)):
            integers[nums[_]].append(_)

        result = 0
        for number, indices in integers.items():
            
            if len(indices) >= 3:
                diff = indices[1] - indices[0]
                for i in range(1, len(indices)):
                    if diff != indices[i] - indices[i - 1]:
                        break
                else:
                    result += 1
        return result