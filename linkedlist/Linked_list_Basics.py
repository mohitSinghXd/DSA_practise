# Make a linked list where you can append, insert and delete elements

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Singly_linked_list:
    def __init__(self):
        self.head = None

    # Append at end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert at any position
    def insert_at(self, value, position):
        new_node = Node(value)

        # Insert at beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        prev_node = None
        count = 0

        while current_node is not None and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        # Invalid position
        if count != position:
            print("Invalid Position")
            return

        prev_node.next = new_node
        new_node.next = current_node

    # Delete by value
    def Delete_at(self, target):

        if self.head is None:
            print("Linked List is Empty")
            return

        # Delete head node
        if self.head.value == target:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return

        prev_node = None
        current_node = self.head

        while current_node is not None and current_node.value != target:
            prev_node = current_node
            current_node = current_node.next

        # Value not found
        if current_node is None:
            print("Value not found")
            return

        prev_node.next = current_node.next
        current_node.next = None
        del current_node

    # Traverse
    def Traverse(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")


# Driver Code

a = Singly_linked_list()

a.append(5)
a.append(10)
a.append(15)
a.append(20)

print("Original List:")
a.Traverse()

print("\nAfter inserting 100 at position 2:")
a.insert_at(100, 2)
a.Traverse()

print("\nAfter deleting 15:")
a.Delete_at(15)
a.Traverse()

print("\nAfter deleting 5:")
a.Delete_at(5)
a.Traverse()