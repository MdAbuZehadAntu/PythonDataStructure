class node:
    def __init__(self, value=None):
        self.right = None
        self.left = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self.__insert(value, self.root)

    def __insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = node(value)
            else:
                self.__insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self.__insert(value, cur_node.right)
        else:
            print("Duplicate value !!! already exists")

    def print_tree(self):
        if self.root is not None:
            self.__print(self.root)

    def __print(self, cur_node):
        if cur_node is not None:
            self.__print(cur_node.left)
            print(f"{cur_node.value}",end=",")
            self.__print(cur_node.right)

    def height(self):
        if self.root is not None:
            return self.__height(self.root, 0)
        else:
            return 0

    def __height(self, cur_node, cur_height):

        if cur_node is None:
            return cur_height
        left_height = self.__height(cur_node.left, cur_height + 1)
        right_height = self.__height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self.__search(value, self.root)
        else:
            return False

    def __search(self, value, cur_node):

        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self.__search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self.__search(value, cur_node.right)
        else:
            return False


bst = BinarySearchTree()
for i in map(int,input().split()):
    bst.insert(i)

bst.print_tree()
print(f"Height of the tree is : {bst.height()}")

if bst.search(4):
    print("Found")
else:
    print("Not found")


