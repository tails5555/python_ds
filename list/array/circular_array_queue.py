# Circular Array Queue Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-31

class CircularQueue :
    # CircularQueue 생성자
    # Merge 연산을 위하여 파라미터 일부 조정
    # 할당 CircularQueue 크기 : size
    def __init__(self, size, data=None, _head=-1, _tail=-1) :
        self.size = size if size > 0 else 1
        self.data = [None] * size if data == None else data
        self._head = _head
        self._tail = _tail

    def is_empty(self) :
        return self._head == self._tail

    def is_full(self) :
        return (self._head + 1) % self.size == self._tail

    def enQueue(self, value) :
        if self.is_full() :
            print('Circular Queue 의 공간이 꽉 찼습니다.')
            return
        else :
            tmp_data = self.data
            tmp_tail = self._tail
            
            next_tail = (tmp_tail + 1) % self.size
            tmp_data[next_tail] = value

            self.data = tmp_data
            self._tail = next_tail

    def deQueue(self) :
        if self.is_empty() :
            print('Circular Queue 의 공간이 비었습니다.')
            return
        else :
            tmp_data = self.data
            tmp_head = self._head

            next_head = (tmp_head + 1) % self.size
            tmp_value = tmp_data[next_head]

            tmp_data[next_head] = None
            
            self.data = tmp_data
            self._head = next_head

            return tmp_value

    def __str__(self) :
        tmp_idx = self._head
        tmp_data = self.data
        result_str = '[ '
        result_cap = 0

        while tmp_idx != self._tail :
            result_cap += 1
            tmp_idx = (tmp_idx + 1) % self.size
            result_str += '{} '.format(tmp_data[tmp_idx])
            
        result_str += '] [Capacity : {}]'.format(result_cap)
        return result_str