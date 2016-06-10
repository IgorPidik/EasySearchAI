__author__ = 'igor'


class PriorityQueue(object):
    def __init__(self):
        self.list = []

    def append(self, x):
        self.list.append(x)

    def __len__(self):
        return len(self.list)

    def pop(self):
        minVal = float('inf')
        index = -1
        for i in range(0, len(self.list)):
            (state, action, cost) = self.list[i]
            if cost < minVal:
                minVal = cost
                index = i

        print("pop index:", index)
        return self.list.pop(index)


class Queue(object):
    def __init__(self):
        self.list = []

    def append(self, x):
        self.list.insert(0, x)

    def pop(self):
        return self.list.pop()

    def __len__(self):
        return len(self.list)


class Stack(object):
    def __init__(self):
        self.list = []

    def append(self, x):
        self.list.append(x)

    def pop(self):
        return self.list.pop()

    def __len__(self):
        return len(self.list)
