class BST:
    def __init__(self, root) -> None:
        self.root = root 
    
    def __str__(self) -> str:
        pass

    def insert(self, data):
        '''recursively insert a new node with given data into tree rooted at self'''
        node = self.root
        if node is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def search(self, data):
        if self.root is None:
            return None
        return self.root.search(data)
    
    def smallest(self):
        if self.root is None:
            return None
        else:
            return self.root.smallest()
    
    def preorder(self):
        if self.root is None:
            return None
        else:
            return self.root.preorder()
        
    def postorder(self):
        if self.root is None:
            return None
        else:
            return self.root.postorder()
    
    def inorder(self):
        if self.root is None:
            return None
        else:
            return self.root.inorder()
    

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return (
            "(" + str(self.data) + "," + str(self.left) + "," + str(self.right) + ")"
        )

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
            
    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data:
            if self.left is None:
                return None
            else:
                self.left.search(data)
        else:
            if self.right is None:
                return None
            return self.right.search(data)
        
    def size(self, data):
        if not self.data:
            return 0
        elif self.right is None and self.left is None:
            return 1
        else:
            return self.right.size(data) + self.left.size(data)
        
    def smallest(self):
        if self.left is None:
            return self
        return self.left.smallest()
    
    def preorder(self):
        return f"(({self.data}), ({self.left.preorder()}), ({self.right.preorder()}))"
    
    def postorder(self):
        return f"{self.left.postorder()}, {self.right.postorder()}, {self.data}"
    
    def inorder(self):
        return f"({self.smallest()}, "


    
