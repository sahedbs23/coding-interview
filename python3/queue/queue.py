from typing import List, Any
from collections import deque


def queue_impl(program: List[str]) -> List[int]:
    queue = deque()
    for instruction in program:
        if instruction == "peak":
            print(queue[0]) if queue else print("Queue is empty!")
        elif instruction == "pop":
            #remove element from the start of the queue
            if queue:
                queue.popleft()
            else:
                print("queue is empty")
        else:
            data = int(instruction[5:])
            queue.append(data)
    return queue


print(queue_impl(["peak", "push 3", "push 2", "pop"]))
