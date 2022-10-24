"""id=72857672."""
import operator


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('error')


def read_input():
    signs = [x for x in input().strip().split(" ")]
    return signs


def solver(arr):
    number_stack = Stack()
    operators = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
        "/": operator.floordiv,
    }
    for element in arr:
        if element not in operators.keys():
            number_stack.push(int(element))
        else:
            b = number_stack.pop()
            a = number_stack.pop()
            result = operators[element](a, b)
            number_stack.push(result)
    return number_stack.items[-1]


if __name__ == "__main__":
    input = read_input()
    result = solver(input)
    print(result)
