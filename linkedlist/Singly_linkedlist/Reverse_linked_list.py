#reverse  a Linked list 


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def reverse_list(self):
        current = self.head 
        stack = [] 
        while current is not None : 
            current_value = stack.append(current.value) 
            current =current.next 
        
        temp = self.head
        while temp is not None :
            temp_value = stack.pop() 
            temp.value = temp_value 
            temp = temp.next 
        
        
       
        
            

# Driver Code
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

ll.traverse()

ll.reverse_list() 

ll.traverse()
 
 
# To reverse a linked a optimal approach should be  approach where no extra space has been taken 

def revserse(self):
    temp = self.head 
    prev  = None 
    while temp is not None:
        front = temp.next  
        temp.next  = head 
        prev  = temp
        temp = front 
        