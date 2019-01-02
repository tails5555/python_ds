# Circular Array Queue Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-31

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
                print('Circular Queue 의 공간이 비었습니다.')
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

for k in range(5, 50, 5) :
    circular_queue1.enQueue(k)
    print(circular_queue1)