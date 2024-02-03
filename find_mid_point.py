
'''
Implement the find_middle_node method for the LinkedList class.

The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.
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
        
my_linked_list = Linked_list(1)
my_linked_list.append(2)
my_linked_list.append(24)
my_linked_list.append(8)
my_linked_list.append(11)
my_linked_list.append(18)
my_linked_list.print_linkedlist()
print(my_linked_list.find_middle_node())

        