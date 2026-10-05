class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]

        for i in s:
            if i == '(':
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    x = 1
                else:
                    x = 2 * x

                stack[-1] += x

        return stack[0]