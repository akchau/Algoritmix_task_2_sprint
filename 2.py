"""id=72826702."""


class StackMax:

    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if self.max_items:
            if item >= self.max_items[-1]:
                self.max_items.append(item)
        else:
            self.max_items.append(item)

    def pop(self):
        if self.items and self.max_items:
            if self.items[-1] == self.max_items[-1]:
                self.max_items.pop()
            return self.items.pop()
        return print('error')

    def get_max(self):
        if self.max_items:
            return self.max_items[-1]
        return None


def read_input():
    signs = [x for x in input().strip().split(" ")]
    return signs


def solver(arr):
    number_stack = StackMax()
    numbers = [str(x) for x in range(-10000, 10000)]
    math_signs = ['+', "-", "*", "/"]
    for element in arr:
        if element in numbers:
            number_stack.push(int(element))
        elif element in math_signs:
            b = number_stack.pop()
            a = number_stack.pop()
            if element == "-":
                result = a - b
            if element == '+':
                result = a + b
            if element == "*":
                result = a * b
            if element == "/":
                result = a // b
            number_stack.push(result)
        else:
            return print('error')
    return number_stack.items[-1]


if __name__ == "__main__":
    input = read_input()
    result = solver(input)
    print(result)
