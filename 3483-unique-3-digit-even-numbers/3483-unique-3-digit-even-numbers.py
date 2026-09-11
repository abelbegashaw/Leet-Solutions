class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        numbers = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if number % 2 == 0 and number > 99:
                            numbers.add(number)
        return len(numbers)