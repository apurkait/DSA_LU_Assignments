class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, data):
        if len(self.stack) == self.size:
            print('Stack Overflow')
            return

        self.stack.append(data)

    # Pop Operation
    def pop(self):
        if not len(self.stack):
            print('Underflow. No elements to remove')
            return

        self.stack.pop()

    def peek(self):
        if not len(self.stack):
            print('Nothing to peek, Stack is already empty')
            return

        return self.stack[-1]


if __name__ == '__main__':
    st = Stack(int(input('Enter the size of the stack: ')))
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)
    print(st.stack)
    print(st.peek())
