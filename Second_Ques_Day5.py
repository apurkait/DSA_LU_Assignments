class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def print_ll(self):
        if not self.head:
            print('Linked List is Empty')
            return

        itr = self.head
        while itr:
            print(itr.data, '-->', end='') if itr.next else print(itr.data)
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.insert_at_end(60)
    ll.print_ll()

