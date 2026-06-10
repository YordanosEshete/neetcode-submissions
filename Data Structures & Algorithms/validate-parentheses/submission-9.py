class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {')':"(" ,   '}':'{',  ']':'['}

        for ltr in s:
            if ltr == '(' or ltr == '{' or ltr == '[':
                stack.append(ltr)
            if ltr == ')' or ltr =='}' or ltr ==']':
                if not stack or stack.pop() != brackets[ltr]:
                    return False

        return len(stack) == 0
        return True

       
        