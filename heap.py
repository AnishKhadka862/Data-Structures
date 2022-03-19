class ContainerEmpty(Exception):
    pass


class Heap:
    def __init__(self):
        self.array = []
        
    def comparator(self, a, b):
        raise NotImplementedError
    
    def push(self, k, v):
        self.array.append((k, v))
        self.heapify_up(len(self.array) - 1)
        return

    def pop(self):
        if len(self.array) == 0:
            raise ContainerEmpty()
        ret = self.array[0]
        self.array[0] = self.array.pop()
        self.heapify_down(0)
        return ret

    def get_top(self):
        if len(self.array) == 0:
            raise ContainerEmpty()
        return self.array[0]

    def heapify_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.comparator(self.array[index][1], self.array[parent_index][1]):
            temp = self.array[parent_index]
            self.array[parent_index] = self.array[index]
            self.array[index] = temp
            self.heapify_up(parent_index)
        return

    def heapify_down(self, index):
        cindex1 = index * 2 + 1
        cindex2 = index * 2 + 2
        new_index = index
        if cindex1 < len(self.array) and \
           self.comparator(self.array[cindex1][1], self.array[new_index][1]):
            new_index = cindex1
        if cindex2 < len(self.array) and \
           self.comparator(self.array[cindex2][1], self.array[new_index][1]):
            new_index = cindex2
        if new_index != index:
            temp = self.array[new_index]
            self.array[new_index] = self.array[index]
            self.array[index] = temp
            self.heapify_down(new_index)
        return
    
    def __str__(self):
        string = '['
        delim = ""
        for item in self.array:
            string += delim
            string += str(item)
            delim = ", "
        string += ']'
        return string


class MinHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def comparator(self, a, b):
        return a < b
            

class MaxHeap(Heap):
    def __init__(self):
        Heap.__init__(self)

    def comparator(self, a, b):
        return a > b

    


x = MinHeap()
y = MaxHeap()
print (x, y)
x.push('A', 14)
y.push('A', 14)
print (x, y)
x.push('B', 10)
y.push('B', 10)
print (x, y)
x.push('C', 11)
y.push('C', 11)
print (x, y)
x.push('D', 12)
y.push('D', 12)
print (x, y)
print (x.pop(), y.pop())
print (x, y)
print (x.get_top(), y.get_top())
print (x, y)
