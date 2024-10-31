class Stack:
    def __init__(self):          # 빈 스택 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가합니다.
        self.items.append(item)
                
    def empty(self):             # 스택이 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            return -1 
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            return -1 
        return self.items[-1]

# 명령 처리 부분
N = int(input())
s = Stack()

for _ in range(N):
    cmd = input().strip()
    if cmd.startswith('push'):
        _, pushnum = cmd.split()
        s.push(int(pushnum))  
    elif cmd == 'pop':
        print(s.pop())
    elif cmd == 'size':
        print(s.size())
    elif cmd == 'empty':
        print(1 if s.empty() else 0)
    elif cmd == 'top':
        print(s.top())