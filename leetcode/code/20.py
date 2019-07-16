class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', ']': '[', '}': '{', '>': '<'}
        
        if len(s) == 0:
            return True
        
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            if s[i] in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                if brackets_map[s[i]] == stack[-1]:
                    print(brackets_map[s[i]])
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True
                