from typing import List, TypeVar, Generic
T = TypeVar('T')
class LinkedList(Generic[T]):
    def __init__(self):
        self.items: List[T]=[]

    def InsetAtEnd(self,x):
        self.items.append(x)

    def ViewList(self):
        return self.items.pop()

