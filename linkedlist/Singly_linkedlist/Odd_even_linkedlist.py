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

    def odd_even(self): 
        odd = self.head 
        even  = self.head.next  
        evenhead = even 
        while even and even.next :
            odd.next = odd.next.next
            odd = odd.next 
            even.next = even.next.next
            even = even.next  
        odd.next = evenhead
        return self.head
            
        
# Driver Code
ll = SinglyLinkedList()

ll.append(2)
ll.append(2)
ll.append(3)
ll.append(40)
ll.append(4) 
ll.append(5)

ll.traverse()


ans = ll.odd_even() 
ll.traverse()