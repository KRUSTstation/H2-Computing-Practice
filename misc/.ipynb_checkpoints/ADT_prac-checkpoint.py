class BST_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_revc(self, data):
        self.root = self.insert_helper(self.root, data)

    def insert_helper(self, root, data):
        node = BST_node(data)

        if root is None:
            return node

        if data < root.data:
            root.left = self.insert_helper(root.left, data)

        elif data > root.data:
            root.right = self.insert_helper(root.right, data)

        return root
    
    def insert_it(self, data):
        previous = None
        current = self.root

        while not current:
            previous = current
            if data < current.data:
                current = current.left
            
            elif data > current.data:
                current = current.right

        if data < previous.data:
            previous.left = BST_node(data)
        
        elif data > previous.data:
            previous.right = BST_node(data)

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, root, data):
        if root is None or root.data == data:
            return root
        
        if data < root.data:
            return self.search_helper(root.left, data)
        
        else:
            return self.search_helper(root.right, data)
        
    def inorder(self):
        result = []
        self.inorder_helper(self.root, result)
        return result

    def inorder_helper(self, root, result):
        if root:
            self.inorder_helper(root.left, result)
            result.append(self.root)
            self.insert_helper(root.right, result)

    