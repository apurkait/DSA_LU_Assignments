class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = self.rear = 0

    def enqueue(self, data):
        if len(self.queue) == self.size:
            print('Queue is already full')
            return
        self.queue.append(data)
        self.rear += 1

    # Dequeue Operation
    def dequeue(self):
        if self.rear == self.front:
            print('Underflow. Queue is already Empty')
            return

        self.queue.pop(0)
        self.rear -= 1


if __name__ == '__main__':
    q = Queue(int(input('Enter size of queue: ')))
    q.dequeue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    print(q.queue)
    print(q.front)
    print(q.rear)
