# Circular Linked List Example
# Writer : tails5555(Kang In Sung)
# Written Date : 2019-01-04

class Node :
    # Circular Linked List 를 만들기 위한 Node 객체 클래스 생성자
    def __init__(self, data=None, next=None, is_root=False) :
        self.data = data
        self.is_root = is_root
        self.next = next

    # 맴버 변수 별 setter, getter 메소드
    def set_data(self, data) :
        self.data = data
    
    def set_is_root(self, is_root) :
        self.is_root = is_root

    def set_next(self, next) :
        self.next = next

    def get_next(self) :
        return self.next

    def get_is_root(self) :
        return self.is_root
        
    def get_data(self) :
        return self.data

    # Node __str__ 메소드
    def __str__(self) :
        if self.next is None :
            return '{} '.format(self.data)
        else :
            return '{} -> '.format(self.data)

class CircularLinkedList :
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
    
    # 순환 연결 리스트 맨 앞에 삽입하는 메소드
    def add_head(self, value) :
        before_node = self.root

        new_node = None

        if before_node is not None :
            before_node.is_root = False
            new_node = Node(value, before_node, True)
        
        else :
            new_node = Node(value, None, True)
            new_node.next = new_node
        
        self.root = new_node
        self.capacity += 1

    # 순환 연결 리스트 맨 마지막에 삽입하는 메소드
    def add_tail(self, value) :
        tmp_node = self.root

        if tmp_node is None :
            self.add_head(value)
            return

        else :
            prev_node = tmp_node
            tmp_node = tmp_node.next

            while tmp_node.is_root is not True :
                prev_node = tmp_node
                tmp_node = tmp_node.next

            prev_node.next = Node(value, self.root, False)

        self.capacity += 1

    # 순환 연결 리스트 __str__ 오버라이딩 메소드
    def __str__(self) :
        tmp_root = self.root
        return ''

circular_linked_list1 = CircularLinkedList()

circular_linked_list1.add_head(10)
print(circular_linked_list1)

