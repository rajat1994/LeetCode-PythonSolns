

class BinarySearchTreeNode :

    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def add_data(self, data):


        if self.data == data:
            return 

        if data < self.data:
            
            if self.left:
                self.left.add_data(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:

            if self.right:
                self.right.add_data(data)

            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    def search(self,data):

        if self.data == data:
            return True

        if data < self.data :

          if self.left:
              return self.left.search(data)

          else:
              return False


        if data > self.data:

          if self.right:
             return self.right.search(data)

          else:
              return False

    def sum(self):

        sum = 0
        
        if self.left:
            sum += self.left.sum()

        sum +=self.data

        if self.right:
            sum += self.right.sum()

        return sum


    def min_node(self):
        if self.left is None:
            return self.data

        return self.left.min_node()

    def max_node(self):
        if self.right is None:
            return self.data

        return self.right.max_node()


    def Delete(self, key):
        if key < self.data:
            if self.left:
             self.left = self.left.Delete(key)

        elif key > self.data:
            if self.right:
             self.right = self.right.Delete(key)

        else :
            if self.left is None and self.right is None:
                return None
            
            elif self.left is None:
                return self.right

            elif self.right is None:
                return self.left

            else:
                min_node = self.right.min_node()
                self.data = min_node
                self.right = self.right.Delete(min_node)

        return self


        
            



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_data(elements[i])
    return root



if __name__ == '__main__':
    numbers = [83,17,50,99,101]
    tree =  build_tree(numbers)
    print(tree.in_order_traversal())
    tree.Delete(50)
    print(tree.in_order_traversal())
    



