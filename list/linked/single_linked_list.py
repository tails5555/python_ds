# Single Linked List Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-29

from copy import copy, deepcopy

class Node :
    # Linked List 를 만들기 위한 Node 객체 클래스 생성자
    # Single Linked List 에선 다음을 가리키는 Node 참조와 이의 값만 저장 되어 있으면 됩니다.
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

    # 맴버 변수 별 setter, getter 메소드
    def set_data(self, data) :
        self.data = data
    
    def set_next(self, next) :
        self.next = next

    def get_next(self) :
        return self.next

    def get_data(self) :
        return self.data

    # Node __str__ 메소드. 마지막 값(즉, next 가 참조하는 값이 없다면) 은 화살표를 없애고 표기합니다.
    # 이외의 값들은 화살표를 붙어줍니다.
    def __str__(self) :
        if self.next is None :
            return '{} '.format(self.data)
        else :
            return '{} -> '.format(self.data)

class SingleLinkedList :
    # Single Linked List 클래스 생성자
    # root 는 Node 를 이용해서 넣을 수 있습니다.
    # 여기서 capacity 는 연결 리스트의 길이입니다.
    def __init__(self, root=None, capacity=0) :
        self.root = root
        self.capacity = 0 if root is None else capacity

    # 맴버 변수 별 setter, getter 메소드
    def set_root(self, root) :
        self.root = root

    def set_capacity(self, capacity) :
        self.capacity = capacity

    def get_root(self) :
        return self.root

    def get_capacity(self) :
        return self.capacity
    
    # 연결 리스트 맨 앞에 삽입하는 메소드
    def add_head(self, value) :
        new_node = Node(value, self.root)
        
        self.root = new_node
        self.capacity += 1

    # 연결 리스트 맨 뒤에 삽입하는 메소드
    def add_tail(self, value) :
        if self.capacity == 0 :
            self.add_head(value)
            return

        tmp_node = self.root

        while tmp_node.get_next() is not None :
            tmp_node = tmp_node.get_next()

        tmp_node.set_next(Node(value))

        self.capacity += 1
        
    # 연결 리스트 인덱스 중간에 삽입하는 메소드
    # 여기서 인덱스가 0번이면 head 삽입, 맨 마지막 인덱스 다음이면 tail 삽입 메소드를 실행합니다.
    # 그리고 인덱스의 이전 노드를 가져오면, 이 친구의 다음 노드를 새로운 노드의 다음 노드로 설정하고, 이전 노드의 다음 노드를 새로운 노드로 저장합니다.
    def add_data(self, idx, value) :
        if self.capacity == 0 :
            if idx > 0 :
                print('아무런 데이터가 들어가지 않아 추가 작업을 취소합니다.')
                return
            else :
                self.add_head(value)

        else :
            if idx < 0 or idx > self.capacity :
                print('유효하지 않은 인덱스를 입력했습니다. 인덱스는 0부터 {} 까지 입력 바랍니다.'.format(self.capacity))
                return
            else :
                if idx == 0 :
                    self.add_head(value)
                elif idx == self.capacity :
                    self.add_tail(value)
                else :
                    new_node = Node(value)
                    prev_node = self.find_by_idx_node(idx - 1)
                    tmp_node = prev_node.get_next()
                    new_node = Node(value, tmp_node)
                    prev_node.set_next(new_node)
                    self.capacity += 1
    
    # 연결 리스트 맨 앞을 삭제하는 메소드
    def remove_head(self) :
        if self.capacity == 0 :
            print('데이터가 아무 것도 없습니다. 데이터를 추가하고 진행하시길 바랍니다.')
            return
        else :
            tmp_node = self.root
            self.root = tmp_node.get_next()
            self.capacity -= 1

    # 연결 리스트 맨 뒤를 삭제하는 메소드
    def remove_tail(self) :
        if self.capacity == 0 :
            print('데이터가 아무 것도 없습니다. 데이터를 추가하고 진행하시길 바랍니다.')
            return
        else :
            prev_node = None
            tmp_node = self.root
            while tmp_node.get_next() is not None :
                prev_node = tmp_node
                tmp_node = tmp_node.get_next()

            prev_node.set_next(None)
            
            self.capacity -= 1

    # 연결 리스트 인덱스 중간을 삭제하는 메소드
    # 여기서 인덱스가 0번이면 head 삭제, 맨 마지막 인덱스 이면 tail 삭제 메소드를 실행합니다.
    def remove_data(self, idx) :
        if self.capacity == 0 :
            if idx > 0 :
                print('데이터가 아무 것도 없습니다. 데이터를 추가하고 진행하시길 바랍니다.')
                return
            else :
                self.add_head(value)
        else :
            if idx < 0 or idx >= self.capacity :
                print('유효하지 않은 인덱스를 입력했습니다. 인덱스는 0부터 {} 까지 입력 바랍니다.'.format(self.capacity - 1))
                return
            else :
                if idx == 0 :
                    self.remove_head()
                elif idx == self.capacity - 1 :
                    self.remove_tail()
                else :
                    prev_node = self.find_by_idx_node(idx - 1)
                    tmp_node = prev_node.get_next()
                    prev_node.set_next(tmp_node.get_next())
                    self.capacity -= 1
        
    # 연결 리스트 인덱스로 찾는 메소드
    def find_by_idx_node(self, idx) :
        tmp_node = self.root
        if tmp_node is not None :
            if idx < 0 or idx >= self.capacity :
                print('유효하지 않은 인덱스를 입력했습니다. 인덱스는 0부터 {} 까지 입력 바랍니다.'.format(self.capacity - 1))
                return None
            
            cnt = 0
            while cnt < idx :
                tmp_node = tmp_node.get_next()
                cnt += 1
                
            return tmp_node

        else :
            return None
    
    # 연결 리스트 데이터로 찾는 메소드
    def find_by_value_idx(self, value) :
        tmp_node = self.root
        
        if tmp_node is None :
            return -1
        
        else :
            idx = 0

            while tmp_node is not None :
                if tmp_node.get_data() == value :
                    return idx
                else :
                    tmp_node = tmp_node.get_next()
                    idx += 1
            
            return -1

    # Single Linked List contains 메소드
    def contains(self, value) :
        tmp_node = self.root

        while tmp_node is not None :
            if tmp_node.get_data() == value :
                return True
            tmp_node = tmp_node.get_next()

        return False
    
    # LinkedList Copy 작업 메소드
    def __copy__(self):
        clazz = self.__class__
        result = clazz.__new__(clazz)
        result.__dict__.update(self.__dict__)
        return result

    # LinkedList Deep Copy 작업 메소드
    def __deepcopy__(self, member):
        clazz = self.__class__
        result = clazz.__new__(clazz)
        member[id(self)] = result

        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, member))

        return result

    # LinkedList __add__ 메소드. LinkedList 끼리 Merge 시키기 위한 연산자 오버로딩
    def __add__(self, another) :
        try :
            if isinstance(another, SingleLinkedList) :
                tmp_list = deepcopy(self)
                tmp_fnode = tmp_list.find_by_idx_node(tmp_list.get_capacity() - 1)

                if tmp_fnode is not None :
                    tmp_fnode.set_next(another.get_root())
                else :
                    tmp_list.set_root(another.get_root())
                
                tmp_list.set_capacity(tmp_list.get_capacity() + another.get_capacity())
                return tmp_list
            
            else :
                raise ArithmeticError('피연산자의 주체가 SingleLinkedList 가 아닙니다.')
        
        except ArithmeticError as exc :
            print('예외 발생 : {}'.format(str(exc)))
    
    # LinkedList __sub__ 메소드. LinkedList 끼리 Minus 시키기 위한 연산자 오버로딩
    def __sub__(self, another) :
        try :
            if isinstance(another, SingleLinkedList) :
                tmp_list = deepcopy(self)
                tmp_node = tmp_list.get_root()

                if tmp_node is not None :
                    while tmp_node is not None :
                        if another.contains(tmp_node.get_data()) :
                            tmp_idx = tmp_list.find_by_value_idx(tmp_node.get_data())
                            if tmp_idx != -1 :
                                tmp_list.remove_data(tmp_idx)

                        tmp_node = tmp_node.get_next()

                return tmp_list

            else :
                raise ArithmeticError('피연산자의 주체가 SingleLinkedList 가 아닙니다.')
        
        except ArithmeticError as exc :
            print('예외 발생 : {}'.format(str(exc)))
    
    # Single Linked List __str__ 메소드
    def __str__(self) :
        tmp_node = self.root
        tmp_str = ''
        
        tmp_str += '[ '
        
        while tmp_node is not None :
            tmp_str += '{}'.format(tmp_node)
            tmp_node = tmp_node.get_next()
        
        tmp_str += '] [Capacity : {}]'.format(self.capacity)

        return tmp_str

# Case 01_1. Add Head Test

single_link_list1 = SingleLinkedList()
print(single_link_list1) # [ ] [Capacity : 0]

single_link_list1.add_head(10)
print(single_link_list1) # [ 10 ] [Capacity : 1]

single_link_list1.add_head(5)
print(single_link_list1) # [ 5 -> 10 ] [Capacity : 2]

# Case 01_2. Add Tail Test

single_link_list1.add_tail(15)
print(single_link_list1) # [ 5 -> 10 -> 15 ] [Capacity : 3]

single_link_list1.add_tail(30)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 30 ] [Capacity : 4]

# Case 01_3. Add Index Test

single_link_list1.add_data(3, 25)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 25 -> 30 ] [Capacity : 5]

single_link_list1.add_data(3, 20)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 20 -> 25 -> 30 ] [Capacity : 6]

# Case 02. Contains Test

print(single_link_list1.contains(10)) # True
print(single_link_list1.contains(20)) # True 
print(single_link_list1.contains(18)) # False

# Case 03_1. Find By Index Test

tmp_second_node = single_link_list1.find_by_idx_node(2)

if tmp_second_node is not None :
    print(tmp_second_node.get_data()) # 15

tmp_sixth_node = single_link_list1.find_by_idx_node(6)

if tmp_sixth_node is not None :
    print(tmp_sixth_node.get_data()) # ...

# Case 03_2. Find By Value To Index Test

print(single_link_list1.find_by_value_idx(15)) # 2
print(single_link_list1.find_by_value_idx(25)) # 4
print(single_link_list1.find_by_value_idx(35)) # -1

# Case 04_1. Remove Head Test

single_link_list1.remove_head()
print(single_link_list1) # [ 10 -> 15 -> 20 -> 25 -> 30 ] [Capacity : 5]

# Case 04_2. Remove Tail Test

single_link_list1.remove_tail()
print(single_link_list1) # [ 10 -> 15 -> 20 -> 25 ] [Capacity : 4]

# Case 04_3. Remove By Index Test

single_link_list1.remove_data(2)
print(single_link_list1) # [ 10 -> 15 -> 25 ] [Capacity : 3]

# Case 05. Linked List Merge Test

single_link_list2 = SingleLinkedList(Node(10), 1)
single_link_list2.add_tail(20)
single_link_list2.add_data(1, 15)
print(single_link_list2) # [ 10 -> 15 -> 20 ] [Capacity : 3]

single_link_list3 = SingleLinkedList(Node(40), 1)
single_link_list3.add_head(30)
print(single_link_list3) # [ 30 -> 40 ] [Capacity : 2]

print(single_link_list2 + single_link_list3) # [ 10 -> 15 -> 20 -> 30 -> 40 ] [Capacity : 5]

# Linked List 간 참조 값이 중복되지 않아 꼬이지 않은 결과가 나오는 것을 각인 시키기 위한 문장입니다.
single_link_list2.add_data(3, 25)
print(single_link_list2) # [ 10 -> 15 -> 20 -> 25 ] [Capacity : 4]

# 아무런 값이 없는 경우에도 LinkedList의 연동이 잘 됨을 각인시키기 위한 문장입니다.
single_link_list4 = SingleLinkedList()

print(single_link_list4 + single_link_list3) # [ 30 -> 40 ] [Capacity : 2]
print(single_link_list3 + single_link_list4) # [ 30 -> 40 ] [Capacity : 2]

print(single_link_list4) # [ ] [Capacity : 0]
print(single_link_list3) # [ 30 -> 40 ] [Capacity : 2]

# 피연산자가 Single Linked List 가 아니면 예외 처리합니다.
single_link_list4 + 5 # 예외 발생 : 피연산자의 주체가 SingleLinkedList 가 아닙니다.

# Case 06. Linked List Minus Test

single_twice_list = SingleLinkedList()
single_triple_list = SingleLinkedList()

for k in range(2, 22, 2) :
    single_twice_list.add_tail(k)

single_twice_list.add_tail(12)

for k in range(3, 33, 3) :
    single_triple_list.add_tail(k)

print(single_twice_list) # [ 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> 12 ] [Capacity : 11]
print(single_triple_list) # [ 3 -> 6 -> 9 -> 12 -> 15 -> 18 -> 21 -> 24 -> 27 -> 30 ] [Capacity : 10]
print(single_twice_list - single_triple_list) # [ 2 -> 4 -> 8 -> 10 -> 14 -> 16 -> 20 ] [Capacity : 7]
print(single_twice_list) # [ 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> 12 ] [Capacity : 11]