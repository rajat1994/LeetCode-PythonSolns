class Node :
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next



class LinkedList :
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        return


    def insert_at_end (self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values (self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    

    def get_length(self):
        counter = 0

        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def remove_at (self, index):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
            

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:

            if counter == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            counter +=1


    def insert_at(self,index,data):
        if index < 0 or self.get_length()<index:
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        counter = 0
        itr = self.head

        new_node = Node(data,None)

        while itr:

            if counter == index-1:
                new_node.next = itr.next
                itr.next = new_node
                break

            itr = itr.next
            counter += 1


    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        lst = ""

        while itr:
            lst += str(itr.data) + "-->"
            itr = itr.next
        print(lst)

    


if __name__ == '__main__':
    ll = LinkedList()
    
    ll.insert_values(['a','b','c','d'])
    ll.print_linked_list()
    ll.insert_at(4,'z')
    ll.print_linked_list()
    ll.remove_at(2)
    ll.print_linked_list()


