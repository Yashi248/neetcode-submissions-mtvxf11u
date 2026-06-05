class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ("+","-","*","/"):
                stack.append(i)
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                if i == "+":
                    c=a+b
                elif i == "-":
                    c=a-b
                elif i == "*":
                    c=a*b
                elif i == "/":
                    c=int(a/b)
                stack.append(c)
        
        return int(stack[0])
