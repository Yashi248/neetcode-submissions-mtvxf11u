class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','*','-','/']
        for n in tokens:
            if n not in operators:
                stack.append(n)
            else:
                a = int(stack.pop())
                b = int(stack.pop()) 
                if n == '+':
                    res = b+a
                    stack.append(res)
                elif n == '-':
                    res = b-a
                    stack.append(res)
                elif n == '*':
                    res = b*a
                    stack.append(res)
                elif n == '/':
                    res = int(b/a)
                    stack.append(res)
        return int(stack[0])
                

