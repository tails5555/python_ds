class Node :
    def __init__(self, value, left=None, right=None) :
        self.value = value
        self.left = left
        self.right = right

    def set_value(self, value) :
        self.value = value

    def set_left(self, left) :
        self.left = left

    def set_right(self, right) :
        self.right = right

    def get_value(self) :
        return self.value

    def get_left(self) :
        return self.left

    def get_right(self) :
        return self.right

    def __str__(self) :
        tmp_value = self.value

        tmp_left = self.left
        tmp_right = self.right

        left_value = tmp_left.get_value() if tmp_left is not None else None
        right_value = tmp_right.get_value() if tmp_right is not None else None

        return '{} - [{}] - {}'.format(left_value, tmp_value, right_value)
        
class BSTree :
    def __init__(self, root=None) :
        self.root = root

    def get_root(self) :
        return self.root

    def insert(self, value) :
        tmp_node = self.root

        if tmp_node is None :
            tmp_node = Node(value)
            self.root = tmp_node

        else :
            while True :
                if tmp_node.get_value() < value :
                    if tmp_node.get_right() is not None :
                        tmp_node = tmp_node.get_right()
                    else :
                        tmp_node.set_right(Node(value))
                        break

                elif tmp_node.get_value() > value :
                    if tmp_node.get_left() is not None :
                        tmp_node = tmp_node.get_left()
                    else :
                        tmp_node.set_left(Node(value))
                        break

                else :
                    print('트리에 이미 존재하는 값이 있습니다.')
                    break
    
    def find_most_right_value_at_left_sub_tree(self, node) :
        if node.get_right() is not None :
            return self.find_most_right_value_at_left_sub_tree(node.get_right())

        return node.get_value()
    
    def delete(self, value, parent=None, child=None) :
        if child is None :
            return

        else :
            if value < child.get_value() :
                if child.get_left() is not None :
                    self.delete(value, child, child.get_left())

            elif value > child.get_value() :
                if child.get_right() is not None :
                    self.delete(value, child, child.get_right())

            else :
                if child.get_left() is not None and child.get_right() is not None :
                    pivot_value = self.find_most_right_value_at_left_sub_tree(child.get_left())
                    child.set_value(pivot_value)
                    self.delete(pivot_value, child, child.get_left())

                else :
                    child_node = child.get_left() if child.get_left() is not None else child.get_right()
                    if parent.get_left() == child :
                        parent.set_left(child_node)
                    else :
                        parent.set_right(child_node)

    def contains(self, value) :
        if self.root is not None :
            tmp_node = self.root
            
            stack = []
            stack.append(tmp_node)
            
            while len(stack) > 0 :
                tmp = stack.pop()

                tmp_left = tmp.get_left()
                tmp_right = tmp.get_right()
                
                if value < tmp.get_value() :
                    if tmp.get_left() is not None :
                        stack.append(tmp.get_left())

                elif value > tmp.get_value() :
                    if tmp.get_right() is not None :
                        stack.append(tmp.get_right())

                else :
                    return True

        return False

    def in_order(self, node) :
        if node is None :
            return

        self.in_order(node.get_left())
        print(node)
        self.in_order(node.get_right())

if __name__ == '__main__' :
    bst_1 = BSTree()
    bst_1.insert(25)
    
    bst_1.insert(15)
    bst_1.insert(35)

    bst_1.insert(10)
    bst_1.insert(20)

    bst_1.insert(30)
    bst_1.insert(40)

    bst_1.insert(45)

    bst_1.in_order(bst_1.get_root())

    """
    None - [10] - None
    10 - [15] - 20
    None - [20] - None
    15 - [25] - 35
    None - [30] - None
    30 - [35] - 40
    None - [40] - 45
    None - [45] - None
    """

    for k in range(5, 51, 5) :
        print(k, bst_1.contains(k))

    """
    5 False
    10 True
    15 True
    20 True
    25 True
    30 True
    35 True
    40 True
    45 True
    50 False
    """

    bst_1.delete(4, None, bst_1.get_root())

    bst_1.in_order(bst_1.get_root())