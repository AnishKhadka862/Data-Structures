# Name: Anish Khadka
# File: llist.py


class KeyError(Exception):
    def __init__(self, k):
        self.k = k
    def __str__(self):
        return f"KeyError: {self.k} not found"


class LList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, k):
        self.head = ListNode(k, None, self.head)
        if self.head.next_ptr is not None:
            self.head.next_ptr.prev_ptr = self.head
        return

    def find(self, k):
        current_ptr = self.head
        while current_ptr is not None:
            if current_ptr.k == k:
                return current_ptr
            current_ptr = current_ptr.next_ptr
        return None

    def delete(self, k):
        current_ptr = self.head
        while current_ptr is not None:
            if current_ptr.k == k:
                prev_ptr = current_ptr.prev_ptr
                next_ptr = current_ptr.next_ptr
                if prev_ptr is not None:
                    prev_ptr.next_ptr = next_ptr
                else:
                    self.head = next_ptr
                if next_ptr is not None:
                    next_ptr.prev_ptr = prev_ptr
                else:
                    self.tail = prev_ptr
                return
            else:
                current_ptr = current_ptr.next_ptr
        raise KeyError(k)

    def __str__(self):
        string = '['
        delim = ''
        current_ptr = self.head
        while current_ptr is not None:
            string += delim
            string += str(current_ptr.k)
            delim = ', '
            current_ptr = current_ptr.next_ptr
        string += ']'
        return string
        
class ListNode:
    def __init__(self, k, prev_ptr=None, next_ptr=None):
        self.k = k
        self.prev_ptr = prev_ptr
        self.next_ptr = next_ptr

    def __str__(self):
        string = "ListNode:"
        string += " id: " + str(id(self))
        string += " key: " + str(self.k)
        string += " prev_ptr: " + str(id(self.prev_ptr))
        string += " next_ptr: " + str(id(self.next_ptr))
        return string
    
x = LList()
x.insert(4)
print (x)
x.insert(5)
print (x)
x.delete(4)
print (x)
x.delete(5)
print (x)
try:
    x.delete(5)
except KeyError as e:
    print (e)
