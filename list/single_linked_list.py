# Single Linked List Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2018-12-29

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
        if self.next == None :
            return '{} '.format(self.data)
        else :
            return '{} -> '.format(self.data)

class SingleLinkedList :
    # Single Linked List 클래스 생성자
    # root 는 Node 를 이용해서 넣을 수 있습니다.
    # 여기서 capacity 는 연결 리스트의 길이입니다.
    def __init__(self, root=None) :
        self.root = root
        self.capacity = 0 if root == None else 1

    # 연결 리스트 맨 앞에 삽입하는 메소드
    def add_head(self, value) :
        new_node = Node(value, self.root)
        
        self.root = new_node
        self.capacity += 1

    # 연결 리스트 맨 뒤에 삽입하는 메소드
    def add_tail(self, value) :
        if self.capacity == 0 :
            self.add_head(value)

        tmp_node = self.root

        while tmp_node.next != None :
            tmp_node = tmp_node.get_next()

        tmp_node.next = Node(value)

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
                    prev_node = self.find_by_idx(idx - 1)
                    tmp_node = prev_node.get_next()
                    new_node = Node(value, tmp_node)
                    prev_node.set_next(new_node)
                    self.capacity += 1
    
    # 연결 리스트 인덱스로 찾는 메소드
    def find_by_idx(self, idx) :
        tmp_node = self.root
        if tmp_node != None :
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
    
    # Single Linked List contains 메소드
    def contains(self, value) :
        tmp_node = self.root

        while tmp_node != None :
            if tmp_node.get_data() == value :
                return True
            tmp_node = tmp_node.get_next()

        return False

    # Single Linked List __str__ 메소드
    def __str__(self) :
        tmp_node = self.root
        tmp_str = ''
        
        tmp_str += '[ '
        
        while tmp_node != None :
            tmp_str += '{}'.format(tmp_node)
            tmp_node = tmp_node.get_next()
        
        tmp_str += '] [Capacity : {}]'.format(self.capacity)

        return tmp_str

# Case 01. Add Head Test

single_link_list1 = SingleLinkedList()
print(single_link_list1) # [ ] [Capacity : 0]

single_link_list1.add_head(10)
print(single_link_list1) # [ 10 ] [Capacity : 1]

single_link_list1.add_head(5)
print(single_link_list1) # [ 5 -> 10 ] [Capacity : 2]

# Case 02. Add Tail Test

single_link_list1.add_tail(15)
print(single_link_list1) # [ 5 -> 10 -> 15 ] [Capacity : 3]

single_link_list1.add_tail(30)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 30 ] [Capacity : 4]

# Case 03. Add Index Test

single_link_list1.add_data(3, 25)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 25 -> 30 ] [Capacity : 5]

single_link_list1.add_data(3, 20)
print(single_link_list1) # [ 5 -> 10 -> 15 -> 20 -> 25 -> 30 ] [Capacity : 6]

# Case 04. Contains Test

print(single_link_list1.contains(10)) # True
print(single_link_list1.contains(20)) # True 
print(single_link_list1.contains(18)) # False

# Case 05. Find By Index Test

tmp_second_node = single_link_list1.find_by_idx(2)

if tmp_second_node != None :
    print(tmp_second_node.get_data()) # 15

tmp_sixth_node = single_link_list1.find_by_idx(6)

if tmp_sixth_node != None :
     print(tmp_sixth_node.get_data()) # ...