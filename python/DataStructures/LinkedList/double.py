from __future__ import annotations
from typing import Any, Union, Literal, NoReturn

class Node():
    value: Any
    next: Union[Node, None]
    prev: Union[Node, None]
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next,
        self.prev = prev


class LinkedList():
    head: Union[Node, None] = None
    tail: Union[Node, None] = None

    def print(self)-> NoReturn:
        node = self.head
        try:
            while node is not None:
                print(node.value)
                node = node.next
        except AttributeError:
            pass
        
    def lpush(self, value: Any)-> NoReturn:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            (self.head, new_node.next, new_node.prev) = (new_node,  self.head, None)

    def rpush(self, value: Any)-> NoReturn:
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            (self.tail, new_node.prev, new_node.next) = (new_node,  self.tail, None)

    def lpop(self)-> Union[Node, None]:
        out = self.head
        try:
            self.head = self.head.next
            self.head.prev = None
        except AttributeError:
            pass
        return out

    def rpop(self)-> Union[Node, None]:
        out = self.tail
        try:
            self.tail = self.tail.prev
            self.tail.next = None
        except AttributeError:
            pass
        return out

    def search(self, value: Any, direction: Literal['left', 'right']='left')-> Union[Node, None]:
        try:
            if direction == 'left':
                node =  self.head
                while (node is not None) & (node.value != value):
                    node = node.next
                return node 
            elif direction == 'right':
                node =  self.tail
                while (node is not None) & (node.value != value):
                    node = node.prev
                return node 
            else:
                raise ValueError('Direction %s is not valid. Selection must be "left" or "right".' % direction)
        except AttributeError:
            return None
        
    def insert(self, value: Any, search_value: Any , position:Literal['before', 'after']='before', direction: Literal['left', 'right']='left')-> NoReturn:
        node = self.search(search_value, direction=direction)

        if node is not None:
            new_node = Node(value)
            if position == 'before':
                new_node.next = node
                new_node.prev =  node.prev
                node.prev.next = new_node
                node.prev = new_node
            elif position == 'after':
                new_node.prev = node
                new_node.next =  node.next
                node.next.prev = new_node
                node.next = new_node
            else:
                ValueError('Position %s is not valid. Selection must be "before" or "after".' % position)

    def delete(self, value: Any, direction: Literal['left', 'right']='left')-> Union[Node, None]:
        node = self.search(value, direction=direction)
        if node is not None:
            (node.next.prev, node.prev.next) = (node.prev, node.next)
        return node
    
    def replace(self, value: Any, new_value: Any, occurrences: Union[int, Literal['all']]=1, direction: Literal['left', 'right']='left', iteration=0):
        n = iteration
        node = self.search(value, direction=direction)

        if node is not None:
            node.value = new_value
            n += 1
            if occurrences == 'all':
                self.replace(value, new_value, occurrences=occurrences, direction=direction, iteration=n)
            elif n < occurrences:
                self.replace(value, new_value, occurrences=occurrences, direction=direction, iteration=n)