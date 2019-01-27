class Node :
    def __init__(self, value, level=0, children=[]) :
        self.value = value
        self.level = level
        self.children = children

    def set_value(self, value) :
        self.value = value

    def get_value(self) :
        return self.value

    def get_children(self) :
        return self.children

    def create_child(self, value) :
        tmp_children = self.children
        tmp_children.append(Node(value, level=self.level + 1, children=[]))

        self.children = tmp_children

    def __str__(self) :
        tmp_children = self.children
        tmp_str = ''

        if len(tmp_children) > 0 :
            for idx, node in enumerate(tmp_children) :
                if idx != len(tmp_children) - 1 :
                    tmp_str += '{} - '.format(node.get_value())
                else :
                    tmp_str += '{}'.format(node.get_value())

            return '{} [Lv. {}] At Children : {}'.format(self.value, self.level, tmp_str)

        else :
            return '{} [Lv. {}] No Children'.format(self.value, self.level)

class ChildrenTree :
    def __init__(self, root=None) :
        self.root = root

    def get_root(self) :
        return self.root

    def dfs(self, node) :
        if node is None :
            return

        print(node)

        for child in node.get_children() :
            self.dfs(child)

    def bfs(self, node) :
        queue = []
        queue.insert(0, node)

        while len(queue) > 0 :
            tmp = queue.pop()
            print(tmp)

            for child in tmp.get_children() :
                queue.insert(0, child)
    
    def contains(self, value) :
        if self.root is not None :
            tmp_node = self.root

            stack = []
            stack.append(tmp_node)

            while len(stack) > 0 :
                tmp = stack.pop()

                if tmp.get_value() == value :
                    return True
                
                for child in tmp.get_children() :
                    stack.append(child)

        return False

    def create_by_command(self, command, value, node) :
        tmp_len = len(command)
        cur_com = command[:1]

        if tmp_len == 0 :
            if node is not None :
                node.create_child(value)
            else :
                print('유효하지 않은 인덱스를 입력하였습니다.')
                return

        else :
            if cur_com.isdigit() :
                tmp_children = node.get_children()
                
                if int(cur_com) < 0 or int(cur_com) > len(tmp_children) :
                    print('인덱스는 0번 부터 {}번 사이로 입력하시길 바랍니다.'.format(len(tmp_children)))
                    return
                
                self.create_by_command(command[1:tmp_len], value, tmp_children[int(cur_com)])
            
            else :
                print('인덱스는 숫자로만 입력하시길 바랍니다.')
                return

"""
            A
      B     C     D
    E   F   G   H I J
        K       L M  
"""
if __name__ == '__main__' :
    children_tree1 = ChildrenTree(root = Node('A'))

    children_tree1.create_by_command('', 'B', children_tree1.get_root())
    children_tree1.create_by_command('', 'C', children_tree1.get_root())
    children_tree1.create_by_command('', 'D', children_tree1.get_root())
    
    children_tree1.create_by_command('0', 'E', children_tree1.get_root())
    children_tree1.create_by_command('0', 'F', children_tree1.get_root())

    children_tree1.create_by_command('1', 'G', children_tree1.get_root())
    
    children_tree1.create_by_command('2', 'H', children_tree1.get_root())
    children_tree1.create_by_command('2', 'I', children_tree1.get_root())
    children_tree1.create_by_command('2', 'J', children_tree1.get_root())

    children_tree1.create_by_command('01', 'K', children_tree1.get_root())

    children_tree1.create_by_command('20', 'L', children_tree1.get_root())
    children_tree1.create_by_command('21', 'M', children_tree1.get_root())

    print('-- Depth First Search Testing --')
    children_tree1.dfs(children_tree1.get_root()) # A B E F K C G D H L I M J

    """
    -- Depth First Search Testing --
    A [Lv. 0] At Children : B - C - D
    B [Lv. 1] At Children : E - F
    E [Lv. 2] No Children
    F [Lv. 2] At Children : K
    K [Lv. 3] No Children
    C [Lv. 1] At Children : G
    G [Lv. 2] No Children
    D [Lv. 1] At Children : H - I - J
    H [Lv. 2] At Children : L
    L [Lv. 3] No Children
    I [Lv. 2] At Children : M
    M [Lv. 3] No Children
    J [Lv. 2] No Children
    """

    print('-- Breadth First Search Testing --')
    children_tree1.bfs(children_tree1.get_root()) # A to M

    """
    A [Lv. 0] At Children : B - C - D
    B [Lv. 1] At Children : E - F
    C [Lv. 1] At Children : G
    D [Lv. 1] At Children : H - I - J
    E [Lv. 2] No Children
    F [Lv. 2] At Children : K
    G [Lv. 2] No Children
    H [Lv. 2] At Children : L
    I [Lv. 2] At Children : M
    J [Lv. 2] No Children
    K [Lv. 3] No Children
    L [Lv. 3] No Children
    M [Lv. 3] No Children
    """

    for a in 'ABCDEFGHIJKLMN' :
        print(a, children_tree1.contains(a))

    """
    A True
    B True
    C True
    D True
    E True
    F True
    G True
    H True
    I True
    J True
    K True
    L True
    M True
    N False
    """