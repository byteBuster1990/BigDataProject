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
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None         
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None        
        return temp
    def prepend(self, value):
        new_node = Node(value)
        old_node = self.head
        if self.head is not None:
            self.head = new_node
            self.head.next = old_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
          
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    

my_linkedlist = Linked_list(21)
my_linkedlist.append(43)
print(my_linkedlist.pop())
my_linkedlist.prepend(23)
print(my_linkedlist.popfirst())