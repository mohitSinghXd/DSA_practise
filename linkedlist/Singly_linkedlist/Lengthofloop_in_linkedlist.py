# If there is a loop in a linked list then find the lenght of it 

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

    def find_length_of_loop(self):
        slow = self.head 
        fast = self.head 
        while fast and fast.next:
            slow  = slow.next 
            fast = fast.next.next 
            
            if slow == fast : 
                count= 0 
                slow = slow.next 
                count +=1 
                while slow != fast:
                    slow = slow.next 
                    count  +=1  
                return count 
        
        return  0     

# Driver Code
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

ll.traverse()


ans = ll.find_middle() 
print(ans.value)