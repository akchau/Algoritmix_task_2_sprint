"""id=72815889."""


class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print("error")

    def push_front(self, x):
        if self.size < self.max_n:
            new_head = (self.head - 1) % self.max_n
            self.queue[new_head] = x
            self.size += 1
            self.head = new_head
        else:
            print("error")

    def pop_front(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    def size(self):
        return self.size


def read_input():
    num = int(input())
    n = int(input())
    my_queue = MyQueueSized(n)
    for num_command in range(num):
        input_commands = [x for x in input().strip().split()]
        command = input_commands[0]
        if command == 'pop_front':
            print(my_queue.pop_front())
        if command == 'pop_back':
            print(my_queue.pop_back())
        elif command == 'size':
            print(my_queue.size)
        elif command == 'push_front':
            value = input_commands[1]
            value = int(value)
            my_queue.push_front(value)
        elif command == 'push_back':
            value = input_commands[1]
            value = int(value)
            my_queue.push_back(value)


if __name__ == "__main__":
    read_input()
