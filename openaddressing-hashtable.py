# Name: Anish Khadka
# File: openaddressing.py

import random; random.seed()
import math

class KeyError(Exception):
    def __init__(self, k):
        self.k = k
    def __str__(self):
        return f"KeyError: {self.k} not found"

class HT:
    AVAILABLE = 0
    NOT_AVAILABLE = 1
    DELETED = 2

    def __init__(self):
        self.a1 = random.randrange(1000000)
        self.b1 = random.randrange(1000000)
        self.p1 = self.generate_big_prime()
        self.a2 = random.randrange(100000)
        self.b2 = random.randrange(100000)
        self.p2 = self.generate_big_prime()
        
        self.length = 8
        self.size = 0
        self.array = [[HT.AVAILABLE, None, None] for _ in range(self.length)]

        
    def is_prime(self, n):
        for div in range(2, int(math.sqrt(n)) + 1):
            if n % div == 0:
                return False
        return True            
        
    def generate_big_prime(self):
        prime_candidate = random.randint(1000000, 500000000)
        if self.is_prime(prime_candidate): return prime_candidate
        return self.generate_big_prime()

    def prehash(self, string):
        prehash = 0
        power = 1
        for c in string:
            prehash += ord(c) * power
            power *= 256
        return prehash
        
    def h(self, h1_output, h2_output, i):
        return (h1_output + h2_output * i) % self.length
    
    def h1(self, prehash):
        return (self.a1 * prehash + self.b1) % self.p1

    def h2(self, prehash):
        tmp = (self.a2 * prehash + self.b2) % self.p2
        return tmp + (tmp % 2 + 1)  # always odd

    def table_resizing(self):
        load_factor = self.size / self.length
        if load_factor < 0.10:
            self.length /= 2
        elif load_factor > 0.5:
            self.length *= 2
        else:
            return
        new_array = [[HT.AVAILABLE, None, None] for _ in range(self.length)]
        for row in self.array:
            if row[0] == HT.NOT_AVAILABLE:
                idx = self.get_insert_index(row[1], new_array)
                new_array[idx] = [HT.NOT_AVAILABLE, row[1], row[2]]
        self.array = new_array
        return
        
    def index_find(self, k):
        prehash = self.prehash(k)
        h1_output = self.h1(prehash)
        h2_output = self.h2(prehash)
        iteration = 0
        while iteration != self.length:
            current_index = self.h(h1_output, h2_output, iteration)
            current_item = self.array[current_index]
            if current_item[0] == HT.AVAILABLE:
                return -1
            elif current_item[0] == HT.NOT_AVAILABLE and current_item[1] == k:
                return current_index
            else:
                iteration += 1
        return -1
    
    def find(self, k):
        index = self.index_find(k)
        if index == -1: raise KeyError(k)
        return self.array[index][2]

    def get_insert_index(self, k, array):
        prehash = self.prehash(k)
        h1_output = self.h1(prehash)
        h2_output = self.h2(prehash)
        iteration = 0
        while iteration != len(array):
            current_index = self.h(h1_output, h2_output, iteration)
            current_item = array[current_index]
            if current_item[0] in [HT.AVAILABLE, HT.DELETED]:
                return current_index
            elif current_item[0] == HT.NOT_AVAILABLE and current_item[1] == k:
                return current_index
            else:
                iteration += 1
        return -1
                         
    def insert(self, k, v):
        index = self.get_insert_index(k, self.array)
        if index == -1:
            raise Exception("TableFull!!!")
        self.array[index] = [HT.NOT_AVAILABLE, k, v]
        self.size += 1
        self.table_resizing()
        return    

    def delete(self, k):
        index = self.index_find(k)
        if index == -1: raise KeyError(k)
        self.array[index][0] = HT.DELETED
        self.size -= 1
        self.table_resizing()
        return
    
    def __str__(self):
        string = '{\n'
        for item in self.array:
            string += '(' + str(item[0]) + ',' + str(item[1]) + ',' + str(item[2]) + ')\n'                 
        string += '}'
        return string


ht = HT()
print (ht)
ht.insert('qqdnsdsdsaasrsdsdrfaa', 2)
print (ht)
ht.insert('qqnqqhdsdsdsdssfgr', 3)
print (ht)
ht.insert('rnqqqqwecfdssdsf', 4)
print (ht)
ht.insert('nsrdsqdsdswwewdffdd', 5)
print (ht)
ht.insert('darfqs', 6)
print (ht)
ht.insert('br', 7)
print (ht)
ht.delete('br')
print (ht)
try:
    ht.delete('br')
except KeyError as e:
    print (e)

