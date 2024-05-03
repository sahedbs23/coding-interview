from typing import List


def execute(program: List[str]) -> List[int]:
    stack = []
    for instruction in program:
        if instruction == 'peak':
            print(stack[-1])
        elif instruction == "pop":
            stack.pop()
        else:
            data = int(instruction[5:])
            stack.append(data)
    return stack


execute(["push 5", "push 3", "pop", "push 4", "push 2", "pop", "pop", "pop"])
