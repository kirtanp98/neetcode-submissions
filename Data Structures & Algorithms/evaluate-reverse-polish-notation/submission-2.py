class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            print(s)
            try:
                num = int(token)
                s.append(num)
            except ValueError:
                r = int(s.pop())
                l = int(s.pop())

                answer = 0

                if token == '+':
                    answer = l+r
                elif token == '-':
                    answer = l-r
                elif token == '*':
                    answer = l*r
                elif token == '/':
                    answer = l/r
                
                s.append(int(answer))
        
        return int(s.pop())