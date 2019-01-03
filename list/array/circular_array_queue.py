# Circular Array Queue Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-31

from copy import deepcopy

# Circular Queue 구현 방법 상, 
class CircularQueue :
    # CircularQueue 생성자
    # Merge 연산을 위하여 파라미터 일부 조정
    # 할당 CircularQueue 크기 : size, _head 와 _tail : Circular Array Queue 의 각각 front, rear
    def __init__(self, size, data=None, _head=-1, _tail=-1) :
        self.size = size if size > 1 else 2
        self.data = [None] * size if data == None else data
        self._head = _head
        self._tail = _tail

    # 맴버 변수 별 setter, getter 메소드
    def set_size(self, size) :
        self.size = size if size > 1 else 2

    def set_data(self, data) :
        self.data = data
    
    def set_head(self, _head) :
        self._head = _head

    def set_tail(self, _tail) :
        self._tail = _tail

    def get_size(self) :
        return self.size

    def get_data(self) :
        return self.data

    def get_head(self) :
        return self._head

    def get_tail(self) :
        return self._tail
    
    # Circular Array Queue 에 데이터가 꽉 차 있는지 확인 시키기 위한 메소드
    def is_full(self) :
        return (self._tail + 1) % self.size == self._head

    # Circular Array Queue 에 데이터가 아무것도 없는지 확인 시키기 위한 메소드
    def is_empty(self) :
        return self._head == -1 and self._tail == -1

    # Circular Array Queue 의 enQueue 연산자 메소드
    def enQueue(self, value) :
        if self.is_full() :
            print('Circular Queue 의 공간이 꽉 찼습니다.')
            return
        else :
            if self.is_empty() :
                self._tail = 0
                self._head = 0

            tmp_data = self.data
            tmp_tail = self._tail
            
            tmp_data[tmp_tail] = value
            next_tail = (tmp_tail + 1) % self.size
            
            self.data = tmp_data
            self._tail = next_tail

    # Circular Array Queue 의 deQueue 연산자 메소드
    def deQueue(self) :
        if self.is_empty() :
            print('Circular Queue 의 공간이 비었습니다.')
            return
        else :
            if self._head == self._tail :
                self._head = -1
                self._tail = -1
                return

            else :
                tmp_data = self.data
                tmp_head = self._head
                
                tmp_value = tmp_data[tmp_head]
                tmp_data[tmp_head] = None
                next_head = (tmp_head + 1) % self.size
                
                self.data = tmp_data
                self._head = next_head

                return tmp_value
    
    # Circular Array Queue contains 메소드
    def contains(self, value) :
        for k in self.data :
            if value == k :
                return True
        
        return False
    
    # Circular Array Queue Deep Copy 작업 메소드
    def __deepcopy__(self, member):
        clazz = self.__class__
        result = clazz.__new__(clazz)
        member[id(self)] = result

        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, member))

        return result

    # Circular Array Queue __add__ 메소드
    def __add__(self, another) :
        tmp_self = deepcopy(self)
        tmp_another = deepcopy(another)
        tmp_queue = CircularQueue(tmp_self.get_size() + tmp_another.get_size() + 1)

        while tmp_self.is_empty() is False :
            tmp_value = tmp_self.deQueue()
            if tmp_value is not None :
                tmp_queue.enQueue(tmp_value)

        while tmp_another.is_empty() is False :
            tmp_value = tmp_another.deQueue()
            if tmp_value is not None :
                tmp_queue.enQueue(tmp_value)

        return tmp_queue

    # Circular Array Queue __sub__ 메소드
    def __sub__(self, another) :
        tmp_self = deepcopy(self)
        tmp_another = deepcopy(another)
        tmp_queue = CircularQueue(tmp_self.get_size())

        while tmp_self.is_empty() is False :
            tmp_value = tmp_self.deQueue()
            if tmp_value is not None :
                if tmp_another.contains(tmp_value) is False :
                    tmp_queue.enQueue(tmp_value)

        return tmp_queue
    
    # Circular Array Queue __str__ 메소드
    def __str__(self) :
        tmp_idx = self._head
        tmp_end = self._tail
        tmp_data = self.data
        result_str = '[ '
        result_cap = 0

        while tmp_idx != tmp_end :
            result_str += '{} '.format(tmp_data[tmp_idx])
            result_cap += 1
            tmp_idx = (tmp_idx + 1) % self.size
            
        result_str += '] [Capacity : {}]'.format(result_cap)
        return result_str

# Case 01. Circular Array Queue enQueue Test

circular_queue1 = CircularQueue(10)
print(circular_queue1) # [ ] [Capacity : 0]

for k in range(5, 50, 5) :
    circular_queue1.enQueue(k)
    print(circular_queue1)

'''
 [ 5 ] [Capacity : 1]
 [ 5 10 ] [Capacity : 2]
 [ 5 10 15 ] [Capacity : 3]
 [ 5 10 15 20 ] [Capacity : 4]
 [ 5 10 15 20 25 ] [Capacity : 5]
 [ 5 10 15 20 25 30 ] [Capacity : 6]
 [ 5 10 15 20 25 30 35 ] [Capacity : 7]
 [ 5 10 15 20 25 30 35 40 ] [Capacity : 8]
 [ 5 10 15 20 25 30 35 40 45 ] [Capacity : 9]
'''

# Case 02. Circular Array Queue deQueue Test

for k in range(1, 5, 1) :
    print(circular_queue1.deQueue())
    print(circular_queue1)

'''
5
[ 10 15 20 25 30 35 40 45 ] [Capacity : 8]
10
[ 15 20 25 30 35 40 45 ] [Capacity : 7]
15
[ 20 25 30 35 40 45 ] [Capacity : 6]
20
[ 25 30 35 40 45 ] [Capacity : 5]

'''

print(circular_queue1.deQueue()) # 25
print(circular_queue1) # [ 30 35 40 45 ] [Capacity : 4]

for k in range(5, 35, 5) :
    circular_queue1.enQueue(k)
    print(circular_queue1)

'''
[ 30 35 40 45 5 ] [Capacity : 5]
[ 30 35 40 45 5 10 ] [Capacity : 6]
[ 30 35 40 45 5 10 15 ] [Capacity : 7]
[ 30 35 40 45 5 10 15 20 ] [Capacity : 8]
[ 30 35 40 45 5 10 15 20 25 ] [Capacity : 9]
Circular Queue 의 공간이 꽉 찼습니다.
[ 30 35 40 45 5 10 15 20 25 ] [Capacity : 9]
Circular Queue 의 공간이 꽉 찼습니다.
[ 30 35 40 45 5 10 15 20 25 ] [Capacity : 9]
'''

# Case 03. Circular Array Queue Merge Test

circular_queue2 = CircularQueue(5)

for k in range(2, 10, 2) :
    circular_queue2.enQueue(k)

circular_queue3 = CircularQueue(10)

for k in range(3, 24, 3) :
    circular_queue3.enQueue(k)

merge_queue = circular_queue2 + circular_queue3
print(merge_queue) # [ 2 4 6 8 3 6 9 12 15 18 21 ] [Capacity : 11]

while merge_queue.is_empty() is False :
    tmp_value = merge_queue.deQueue()
    if tmp_value is not None :
        print(tmp_value)

'''
2
4
6
8
3
6
9
12
15
18
21
'''

print(circular_queue2) # [ 2 4 6 8 ] [Capacity : 4]
print(circular_queue3) # [ 3 6 9 12 15 18 21 ] [Capacity : 7]

# Case 04. Circular Array Queue Minus Test

circular_queue4 = CircularQueue(10)

for k in range(4, 40, 4) :
    circular_queue4.enQueue(k)

circular_queue5 = CircularQueue(10)

for k in range(6, 60, 6) :
    circular_queue5.enQueue(k)

print(circular_queue4) # [ 4 8 12 16 20 24 28 32 36 ] [Capacity : 9]
print(circular_queue5) # [ 6 12 18 24 30 36 42 48 54 ] [Capacity : 9]

minus_queue1 = circular_queue4 - circular_queue5
print(minus_queue1) # [ 4 8 16 20 28 32 ] [Capacity : 6]

while minus_queue1.is_empty() is False :
    tmp_value = minus_queue1.deQueue()
    if tmp_value is not None :
        print(tmp_value)

'''
4
8
16
20
28
32
'''

minus_queue2 = circular_queue5 - circular_queue4
print(minus_queue2) # [ 6 18 30 42 48 54 ] [Capacity : 6]

while minus_queue2.is_empty() is False :
    tmp_value = minus_queue2.deQueue()
    if tmp_value is not None :
        print(tmp_value)

'''
6
18
30
42
48
54
'''

# Case 05. Circular Array Queue Contains Method Test

# 참고로 연산을 진행한 후의 Circular Queue 는 원래 값 그대로 유지하고 있어 아래 문장을 실행하는데 문제가 되지 않습니다.

print(circular_queue2.contains(2)) # True
print(circular_queue2.contains(5)) # False
