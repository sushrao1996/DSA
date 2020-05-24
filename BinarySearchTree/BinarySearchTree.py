class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self,root=None):
        self.root=None
    def get_root(self):
        return self.root
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self.insert_helper(self.root,key)
    def insert_helper(self,this_node,key):
        if this_node.key>key:
            if this_node.left is None:
                this_node.left=Node(key)
            else:
                self.insert_helper(this_node.left,key)
        else:
            if this_node.right is None:
                this_node.right=Node(key)
            else:
                self.insert_helper(this_node.right,key)
    def find_inorder_successor(self,this_node):
        myval=this_node
        while myval.left is not None:
            myval=myval.left
        return myval
    def find_inorder_predecessor(self,this_node):
        myval=this_node
        while myval.right is not None:
            myval=myval.right
        return myval
    def search(self,this_node,key):
        if this_node is None:
            print("Key not found")
            return
        elif this_node.key==key:
            print("Key was found")
            return
        elif key<this_node.key:
            self.search(this_node.left,key)
        else:
            self.search(this_node.right,key)
    def inorder(self,this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.key,',',end=" ")
            self.inorder(this_node.right)
    def preorder(self,this_node):
        if this_node:
            print(this_node.key,',',end=" ")
            self.preorder(this_node.left)
            self.preorder(this_node.right)
    def postorder(self,this_node):
        if this_node:
            self.postorder(this_node.left)
            self.postorder(this_node.right)
            print(this_node.key,',',end=" ")
tree = BinarySearchTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.inorder(tree.root))
