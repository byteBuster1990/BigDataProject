
'''
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:



Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.


'''

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
    
    def find_middle_node(self):
        if self.head == None:
            return None
        
        forward = self.head
        mid = self.head
        while forward.next != None:
            forward = forward.next
            if forward.next != None:
                forward = forward.next
            mid = mid.next
        return mid.value
    def has_loop(self):
        if self.head == None:
            return None
        
        forward = self.head
        mid = self.head
        while forward.next != None:
            forward = forward.next
            if forward.next != None:
                forward = forward.next
            else:
               return False 
            mid = mid.next
            if forward == mid:
                return True

     
        
        


        
my_linked_list = Linked_list(1)
my_linked_list.append(2)
my_linked_list.append(24)
my_linked_list.append(8)
my_linked_list.append(11)
my_linked_list.append(18)
my_linked_list.print_linkedlist()
print(my_linked_list.find_middle_node())

        