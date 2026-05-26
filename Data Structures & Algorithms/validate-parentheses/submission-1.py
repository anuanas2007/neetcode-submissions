class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "({["

        for i in s:
            if i in open:
                stack.append(i)
            
            else:
                if not stack:
                    return False
                if i == "}" and stack.pop() != "{":
                    return False
                if i == "]" and stack.pop() != "[":
                    return False
                if i == ")" and stack.pop() != "(":
                    return False
        return stack == []
        