# ArrayList Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-25

class ArrayList :
    # ArrayList 생성자
    # Merge 연산을 위하여 파라미터 일부 조정
    # 할당 ArrayList 길이 : size, 실제 ArrayList 길이 : capacity
    def __init__(self, size, capacity=0, data=None) :
        self.size = size
        self.capacity = capacity
        self.data = [None] * size if data == None else data

    # 각 멤버 변수 별 Setter 작성
    def set_data(self, data) :
        self.data = data

    def set_size(self, size) :
        self.size = size

    def set_capacity(self, capacity) :
        self.capacity = capacity
    
    # 각 멤버 변수 별 Getter 작성
    def get_data(self) :
        return self.data

    def get_size(self) :
        return self.size

    def get_capacity(self) :
        return self.capacity
    
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

    # ArrayList 에 데이터 포함을 확인하는 메소드
    def contains(self, value) :
        tmp_list = self.data
        res = False
        for i in tmp_list :
            if i == value :
                res = True
                break
                
        return res

    # ArrayList 에 데이터의 인덱스를 가져오는 메소드
    def index_of(self, value) :
        tmp_list = self.data
        for (idx, k) in enumerate(tmp_list) :
            if k == value :
                return idx

        return -1

    # ArrayList __add__ 메소드. ArrayList 끼리 Merge 시키기 위한 연산자 오버로딩
    def __add__(self, another) :
        try :
            if isinstance(another, ArrayList) :
                tmp_size = self.size + another.get_size()
                tmp_array_list = ArrayList(tmp_size)
            
                my_data = self.data
                ano_data = another.data
                
                for k in my_data :
                    if k != None :
                        tmp_array_list.add_first(k)
                    else : 
                        break
                
                for k in ano_data :
                    if k != None :
                        tmp_array_list.add_first(k)
                    else : 
                        break

                return tmp_array_list
            
            else :
                raise ArithmeticError('피연산자의 주체가 ArrayList 가 아닙니다.')
        
        except ArithmeticError as exc :
            print('예외 발생 : {}'.format(str(exc)))
    
    # ArrayList __sub__ 메소드. ArrayList 차집합(Minus) 을 위한 연산자 오버로딩
    def __sub__(self, another) :
        try :
            if isinstance(another, ArrayList) :
                ano_data = another.data
                tmp_array_list = ArrayList(self.get_size(), self.get_capacity(), self.get_data())
                
                for (idx, k) in enumerate(tmp_array_list.get_data()) :
                    for l in ano_data :
                        if l == None :
                            break
                        if k == l :
                            tmp_array_list.remove_data(tmp_array_list.index_of(l))

                return tmp_array_list
            
            else :
                raise ArithmeticError('피연산자의 주체가 ArrayList 가 아닙니다.')
        
        except ArithmeticError as exc :
            print('예외 발생 : {}'.format(str(exc)))

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

# Case 01. 데이터 추가 및 동적 길이 증가 확인

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

# Case 02. 데이터 삭제 및 동적 길이 감소 확인

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

# Case 03. 데이터 포함 메소드, 데이터 인덱스 테스트

array_list1.add_data(1, 20)
print(array_list1.contains(10)) # True
print(array_list1.index_of(20)) # 1
print(array_list1.index_of(30)) # -1

# Case 04. ArrayList Merge 연산 테스트

array_list2 = ArrayList(2)
array_list3 = ArrayList(3)

array_list2.add_first(10)
array_list2.add_first(20)

print(array_list2) # [ 20 10 - - ][Capacity : 2] 길이가 2배로 늘어납니다.

array_list3.add_last(5)
array_list3.add_last(15)
array_list3.add_last(25)

print(array_list3) # [ 5 15 25 - - - ][Capacity : 3] 길이가 2배로 늘어납니다.

print(array_list2 + array_list3) # [ 20 10 5 15 25 - - - - - ][Capacity : 5]
print(array_list2) # [ 20 10 - - ][Capacity : 2] 원래 값들은 그대로 유지되고, 객체에 대한 연산의 결과만 반환 시켰습니다.

# 피연산자가 ArrayList 가 아니면 예외 처리합니다.
array_list2 + 20 # 예외 발생 : 피연산자의 주체가 ArrayList 가 아닙니다.

# Case 05. ArrayList Minus 연산 테스트

array_list4 = ArrayList(5)
array_list5 = ArrayList(5)

for k in range(10, 110, 10) :
    array_list4.add_first(k)

print(array_list4) # [ 100 90 80 70 60 50 40 30 20 10 - - - - - - - - - - ][Capacity : 10]

for l in range(20, 220, 20) :
    array_list5.add_last(l)

print(array_list5) # [ 20 40 60 80 100 120 140 160 180 200 - - - - - - - - - - ][Capacity : 10]

print(array_list4 - array_list5) # [ 90 70 50 30 10 ][Capacity : 5]

# 원래 값들은 그대로 유지되고, 객체에 대한 연산의 결과만 반환 시켰습니다.
print(array_list4) # [ 90 80 70 60 50 40 30 20 10 - - - - - - - - - - - ][Capacity : 10]

# 피연산자가 ArrayList 가 아니면 예외 처리합니다.
array_list4 + 20 # 예외 발생 : 피연산자의 주체가 ArrayList 가 아닙니다.