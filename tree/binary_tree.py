class Node :
    def __init__(self, value, level=0, left=None, right=None) :
        self.level = level
        self.value = value
        self.left = left
        self.right = right

    def set_value(self, value) :
        self.value = value
    
    def get_left(self) :
        return self.left

    def get_right(self) :
        return self.right
    
    def create_left_child(self, value) :
        tmp_lev = self.level
        self.left = Node(value, tmp_lev + 1)

    def create_right_child(self, value) :
        tmp_lev = self.level
        self.right = Node(value, tmp_lev + 1)

    def __str__(self) :
        tmp_left = self.left
        left_val = None if tmp_left is None else tmp_left.value
        
        tmp_right = self.right
        right_val = None if tmp_right is None else tmp_right.value
        
        return '{} - {} - {} (Level. {})'.format(left_val, self.value, right_val, self.level)

class Tree :
    def __init__(self, root=None) :
        self.root = root

    def get_root(self) :
        return self.root

    def pre_order(self, node) :
        if node == None :
            return

        print(node)
        self.pre_order(node.get_left())
        self.pre_order(node.get_right())

    def in_order(self, node) :
        if node == None :
            return

        self.in_order(node.get_left())
        print(node)
        self.in_order(node.get_right())

    def post_order(self, node) :
        if node == None :
            return

        self.post_order(node.get_left())
        self.post_order(node.get_right())
        print(node)

    def level_order(self, node) :
        queue = []
        queue.insert(0, node)

        while len(queue) > 0 :
            tmp = queue.pop()
            print(tmp)

            if tmp.get_left() is not None :
                queue.insert(0, tmp.get_left())

            if tmp.get_right() is not None :
                queue.insert(0, tmp.get_right())

    def create_by_command(self, command, value, node) :
        tmp_len = len(command)
        cur_com = command[:1]

        if tmp_len == 1 :
            if cur_com == 'L' :
                if node.get_left() is None :
                    node.create_left_child(value)
                
                else :
                    print('해당 명령어에 이미 존재하는 값이 있어 삽입을 하지 않겠습니다.')

            elif cur_com == 'R' :
                if node.get_right() is None :
                    node.create_right_child(value)
                
                else :
                    print('해당 명령어에 이미 존재하는 값이 있어 삽입을 하지 않겠습니다.')
            
            else :
                print('명령어는 L, R 로만 작성하시길 바랍니다.')

            return

        if cur_com == 'L' :
            if node.get_left() is not None :
                self.create_by_command(command[1:tmp_len], value, node.get_left())
            else :
                print('현재 시점에서 해당되는 Node 가 존재하지 않아 삽입 과정을 중단합니다.')

        elif cur_com == 'R' :
            if node.get_right() is not None :
                self.create_by_command(command[1:tmp_len], value, node.get_right())
            else :
                print('현재 시점에서 해당되는 Node 가 존재하지 않아 삽입 과정을 중단합니다.')

        else :
            print('명령어는 L, R 로만 작성하시길 바랍니다.')

#           A
#       B       C 
#     D   E       F
#    G H   I     J K
if __name__ == '__main__' :
    tree_1 = Tree(root = Node('A'))

    tree_1.create_by_command('L', 'B', tree_1.get_root())
    tree_1.create_by_command('R', 'C', tree_1.get_root())
    tree_1.create_by_command('LL', 'D', tree_1.get_root())
    tree_1.create_by_command('LR', 'E', tree_1.get_root())
    tree_1.create_by_command('RR', 'F', tree_1.get_root())
    tree_1.create_by_command('LLL', 'G', tree_1.get_root())
    tree_1.create_by_command('LLR', 'H', tree_1.get_root())
    tree_1.create_by_command('LRR', 'I', tree_1.get_root())
    tree_1.create_by_command('RRL', 'J', tree_1.get_root())
    tree_1.create_by_command('RRR', 'K', tree_1.get_root())
    
    tree_1.create_by_command('RRR', 'L', tree_1.get_root()) # 이미 명령어에 따라 탐색하는 Node 에 값이 존재함.
    tree_1.create_by_command('LRLL', '?', tree_1.get_root()) # 만들어진 트리에 무효한 명령어로 시도하면 삽입 과정이 중단됨.

    print('-- Tree Pre Order --') # 전위 순회 시작
    tree_1.pre_order(tree_1.get_root()) # A B D G H E I C F J K

    """
        -- Tree Pre Order --
        B - A - C (Level. 0)
        D - B - E (Level. 1)
        G - D - H (Level. 2)
        None - G - None (Level. 3)
        None - H - None (Level. 3)
        None - E - I (Level. 2)
        None - I - None (Level. 3)
        None - C - F (Level. 1)
        J - F - K (Level. 2)
        None - J - None (Level. 3)
        None - K - None (Level. 3)
    """

    print('-- Tree In Order --') # 중위 순회 시작
    tree_1.in_order(tree_1.get_root()) # G D H B E I A C J F K

    """
        -- Tree In Order --
        None - G - None (Level. 3)
        G - D - H (Level. 2)
        None - H - None (Level. 3)
        D - B - E (Level. 1)
        None - E - I (Level. 2)
        None - I - None (Level. 3)
        B - A - C (Level. 0)
        None - C - F (Level. 1)
        None - J - None (Level. 3)
        J - F - K (Level. 2)
        None - K - None (Level. 3)
    """

    print('-- Tree Post Order --') # 후위 순회 시작
    tree_1.post_order(tree_1.get_root()) # G H D I E B J K F C A

    """
        -- Tree Post Order --
        None - G - None (Level. 3)
        None - H - None (Level. 3)
        G - D - H (Level. 2)
        None - I - None (Level. 3)
        None - E - I (Level. 2)
        D - B - E (Level. 1)
        None - J - None (Level. 3)
        None - K - None (Level. 3)
        J - F - K (Level. 2)
        None - C - F (Level. 1)
        B - A - C (Level. 0)
    """

    print('-- Tree Level Order --') # 레벨 순회 시작
    tree_1.level_order(tree_1.get_root()) # A B C D E F G H I J K

    """
        -- Tree Level Order --
        B - A - C (Level. 0)
        D - B - E (Level. 1)
        None - C - F (Level. 1)
        G - D - H (Level. 2)
        None - E - I (Level. 2)
        J - F - K (Level. 2)
        None - G - None (Level. 3)
        None - H - None (Level. 3)
        None - I - None (Level. 3)
        None - J - None (Level. 3)
        None - K - None (Level. 3)
    """