class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack:
                    return False
                next_val = stack.pop(-1)
                if next_val != matches[char]:
                    return False
        if stack:
            return False
        return True