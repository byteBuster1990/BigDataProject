class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

my_linkedlist = Linked_list(21)
my_linkedlist.append(43)
my_linkedlist.print_linkedlist()
