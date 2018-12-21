class ArrayList :
    # ArrayList 생성자
    def __init__(self, size) :
        self.size = size # 할당 ArrayList 길이
        self.capacity = 0 # 실제 ArrayList 길이
        self.data = [None] * size # ArrayList 데이터 목록

    # Index 와 값으로 ArrayList 삽입 메소드
    def add_data(self, idx, value) :
        tmp_list = self.data
        
        if idx > self.capacity :
            print('ArrayList 의 인덱스를 다시 확인하세요. 인덱스는 {} 까지 가능합니다.'.format(self.capacity))
            return

        if len(tmp_list) > 0 :
            for i in range(self.capacity, idx, -1) :
                tmp_list[i] = tmp_list[i - 1]

        tmp_list[idx] = value
        
        self.capacity += 1
        if self.capacity >= self.size :
            tmp_list = tmp_list + [None] * self.size
            self.size *= 2

        self.data = tmp_list
        

    # ArrayList 처음 자리에 값을 추가하는 메소드
    def add_first(self, value) :
        self.add_data(0, value)
    
    # ArrayList 마지막 자리에 값을 추가하는 메소드
    def add_last(self, value) :
        self.add_data(self.capacity, value)

    # Index 값으로 ArrayList 삭제 메소드
    def remove_data(self, idx) :
        tmp_list = self.data

        if idx >= self.capacity :
            print('ArrayList 의 인덱스를 다시 확인하세요. 인덱스는 {} 까지 가능합니다.'.format(self.capacity))
            return
        
        tmp_list[idx] = None
        
        if len(tmp_list) > 0 :
            for i in range(idx, self.capacity) :
                if i < self.capacity - 1:
                    tmp_list[i] = tmp_list[i + 1]
                else :
                    tmp_list[i] = None

        self.capacity -= 1
        if self.capacity <= self.size // 2 and self.size > 1 :
            self.size //= 2
            tmp_list = tmp_list[0:self.size]

        self.data = tmp_list

    # ArrayList 처음 자리 값을 삭제하는 메소드 
    def remove_first(self) :
        self.remove_data(0)
    
    # ArrayList 마지막 자리 값을 삭제하는 메소드 
    def remove_last(self) :
        self.remove_data(self.capacity - 1)

    # ArrayList __str__ 메소드
    def __str__(self) :
        tmp_list = self.data
        result_str = ''
        for i in tmp_list :
            if i != None :
                result_str += '{} '.format(i)
            else :
                result_str += '{} '.format('-')

        return '[ {}][Capacity : {}]'.format(result_str, self.capacity)

array_list1 = ArrayList(5)

array_list1.add_first(10)
print(array_list1) # [ 10 - - - - ][Capacity : 1]

array_list1.add_last(20)
print(array_list1) # [ 10 20 - - - ][Capacity : 2]

array_list1.add_first(30)
print(array_list1) # [ 30 10 20 - - ][Capacity : 3]

array_list1.add_data(1, 40)
print(array_list1) # [ 30 40 10 20 - ][Capacity : 4]

array_list1.add_data(2, 50) # 여기서 ArrayList 의 길이가 2배로 늘어납니다.
print(array_list1) # [ 30 40 50 10 20 - - - - - ][Capacity : 5]

array_list1.add_data(1, 60) 
print(array_list1) # [ 30 60 40 50 10 20 - - - - ][Capacity : 6]

array_list1.remove_first() # 여기서 ArrayList 의 길이가 1/2배로 줄어듭니다.
print(array_list1) # [ 60 40 50 10 20 ][Capacity : 5]

array_list1.remove_data(1) 
print(array_list1) # [ 60 50 10 20 - ][Capacity : 4]

array_list1.remove_last()
print(array_list1) # [ 60 50 10 - - ][Capacity : 3]

array_list1.remove_first() # 여기서 ArrayList 의 길이가 1/2배로 줄어듭니다.
print(array_list1) # [ 50 10 ][Capacity : 2]

array_list1.remove_data(1) # 여기서도 ArrayList 의 길이가 1/2배로 줄어듭니다.
print(array_list1) # [ 50 ][Capacity : 1]

array_list1.remove_first()
print(array_list1) # [ - ][Capacity : 0]

array_list1.add_data(0, 10) # 여기서 ArrayList 의 길이가 2배로 늘어납니다.
print(array_list1) # [ 10 - ][Capacity : 1]

array_list1.add_last(10) # 여기서도 ArrayList 의 길이가 2배로 늘어납니다.
print(array_list1) # [ 10 10 - - ][Capacity : 2]