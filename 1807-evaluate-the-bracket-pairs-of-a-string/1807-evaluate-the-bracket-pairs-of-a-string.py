class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        result = []
        stack = []
        knowledge = {
            idx : val for idx, val in knowledge
        }
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                result.append(knowledge.get("".join(stack), '?'))
                stack.clear()
            else:
                if stack:
                    stack.append(char)
                else:
                    result.append(char)
        return "".join(result)