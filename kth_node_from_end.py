
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

         

def  find_kth_from_end(appned_list, kthvalue):
# get_new_node = Linked_list(value)
    
    if kthvalue != 0:
        fwd = appned_list.head
        kth_value = appned_list.head

        for _ in range (0, kthvalue - 1):
            fwd = fwd.next
        
            if fwd == None:
                return None
         
        while fwd.next != None:            
            fwd = fwd.next
            kth_value = kth_value.next
        return kth_value.value
    else:
        return None   


        



my_linked_list = Linked_list(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
print(result)  # Output: 4

        