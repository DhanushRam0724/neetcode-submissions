class Solution:

    def checkNegative(self, ch):
        if ch.startswith("-"):
            return len(ch) > 1 and ch[1:].isdigit()
        return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for ch in tokens:
            if ch.isdigit() or self.checkNegative(ch):
                stack.append(int(ch))

            elif ch == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)

            elif ch == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif ch == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)

            elif ch == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

        return stack[-1]
