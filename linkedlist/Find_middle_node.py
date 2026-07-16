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

    # Tumhe ye function complete karna hai
    def find_middle(self): 
         slow = self.head 
         fast  = self.head
         while fast is not None and fast.next is not None :
             slow = slow.next 
             fast = fast.next.next
          
         return slow

# Driver Code
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

ll.traverse()

# Yahan call karna
ans = ll.find_middle() 
print(ans.value)