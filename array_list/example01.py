class ArrayList :
    def __init__(self, size) :
        self.size = size
        self.capacity = 0
        self.data = [None] * size

    def add_data(self, idx, value) :
        tmp_list = self.data
        
        if idx > self.capacity :
            print('ArrayList 의 인덱스를 다시 확인하세요. 인덱스는 {} 까지 가능합니다.'.format(self.capacity))
            return

        if self.capacity >= self.size :
            tmp_list = tmp_list + [None] * self.size
            self.size *= 2
        
        if len(tmp_list) > 0 :
            for i in range(self.capacity, idx, -1) :
                tmp_list[i] = tmp_list[i - 1]

        tmp_list[idx] = value

        self.data = tmp_list
        self.capacity += 1

    def add_first(self, value) :
        self.add_data(0, value)
    
    def add_last(self, value) :
        self.add_data(self.capacity, value)

    def __str__(self) :
        return '{}'.format(self.data)

array_list1 = ArrayList(5)

array_list1.add_first(10) # [10]
array_list1.add_last(20) # [10, 20]
array_list1.add_first(30) # [30, 10, 20]
array_list1.add_data(1, 40) # [30, 40, 10, 20]
array_list1.add_data(2, 50) # [30, 40, 50, 10, 20]
array_list1.add_data(1, 60) # 여기서 ArrayList 의 길이가 2배로 늘어납니다.
print(array_list1) # [30, 60, 40, 50, 10, 20, None, None, None, None]