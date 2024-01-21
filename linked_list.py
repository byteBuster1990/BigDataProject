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
    
    def get_value(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
        return temp.value
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        return self.get_value(index).value
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range (self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    

my_linkedlist = Linked_list(1)
my_linkedlist.append(2)
my_linkedlist.append(3)
# my_linkedlist.prepend(23)
# my_linkedlist.get_value(2)
# print(my_linkedlist.insert(2,56))
# print(my_linkedlist.remove(0))
# my_linkedlist.print_linkedlist()
my_linkedlist.reverse()
my_linkedlist.print_linkedlist()
