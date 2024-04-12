from typing import Optional

class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        elif node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        else:
            return False  # Overlapping events

class Calendar():
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        else:
            return self.root.insert(Node(start, end))

# Test the Calendar class
calendar = Calendar()
print(calendar.book(5, 10))  # Expect True
print(calendar.book(8, 13))  # Expect False
print(calendar.book(10, 15))  # Expect True
