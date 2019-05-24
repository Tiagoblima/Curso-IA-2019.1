from collections import defaultdict


class Graph:
    def __init__(self, start, end):
        self.edges = defaultdict(list)

    def add_edge(self, source, destination, cost):
        self.edges[source].append((destination, cost))


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)


class Queue:

    def __init__(self):
        self.queue = []

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item, priority):
        self.queue.append((item, priority))
        sorted(self.queue, key=lambda p: p[1])
