"""id=72852957."""


class MyQueueSized:
    def __init__(self, max_length):
        self.__queue = [None] * max_length
        self.__max_n = max_length
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def _is_empty(self):
        return self.__size <= 0

    def _is_full(self):
        return self.__size >= self.__max_n

    def _count_index(self, current_index, minus=1):
        result = (current_index + 1 * minus) % self.__max_n
        return result

    def push_back(self, x):
        if self._is_full():
            return "error"
        else:
            self.__queue[self.__tail] = x
            self.__tail = self._count_index(self.__tail)
            self.__size += 1

    def push_front(self, x):
        if self._is_full():
            return "error"
        else:
            new_head = self._count_index(self.__head, -1)
            self.__queue[new_head] = x
            self.__size += 1
            self.__head = new_head

    def pop_front(self):
        if self._is_empty():
            return "error"
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self._count_index(self.__head)
        self.__size -= 1
        return x

    def pop_back(self):
        if self._is_empty():
            return "error"
        x = self.__queue[self.__tail-1]
        self.__queue[self.__tail-1] = None
        self.__tail = self._count_index(self.__tail, -1)
        self.__size -= 1
        return x

    def get_size(self):
        return self.__size


def read_input():
    num = int(input())
    n = int(input())
    my_queue = MyQueueSized(n)
    for num_command in range(num):
        command, *value = [x for x in input().strip().split()]
        a = getattr(my_queue, command)(*value)
        if a:
            print(a)


if __name__ == "__main__":
    read_input()
