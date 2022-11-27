
# Design a class that accommodates all the Tree traversal types (Inorder, Preorder, Postorder)
class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
class Tree:
    def __init__(self,root):
        self.root = root
        
    def pre_order(self):
        self.__pre_order_helper(self.root)
        print()
    
    def post_order(self):
        self.__post_order_helper(self.root)
        print()
    
    def in_order(self):
        self.__inorder_helper(self.root)
        print()
    
    def __inorder_helper(self,rt):
        if rt == None:
            return
        self.__inorder_helper(rt.left)
        print(rt.val,end=" ")
        self.__inorder_helper(rt.right)
    
    def __post_order_helper(self,rt):
        if rt == None:
            return
        self.__post_order_helper(rt.left)
        self.__post_order_helper(rt.right)
        print(rt.val,end=" ")
    
    def __pre_order_helper(self,rt):
        if rt == None:
            return
        print(rt.val,end=" ")
        self.__pre_order_helper(rt.left)
        self.__pre_order_helper(rt.right)
        
    
        


if __name__=="__main__":
    tree = '''
      1
    /   \\
   2     3
  / \\   / \\
 4   5 6   7
    '''
    print(tree)
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    
    tree = Tree(root)
    print("The Pre order traversal of above tree:")
    tree.pre_order()
    print("The post order traversal of above tree:")
    tree.post_order()
    print("The in order traversal of above tree:")
    tree.in_order()
    
