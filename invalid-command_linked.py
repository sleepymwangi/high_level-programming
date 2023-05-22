class DoubleLinkedListNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

    def push(self, obj):
        new_node = DoubleLinkedListNode(obj, None, None)
        if self.next is None:
            self.next = new_node
            new_node.prev = self
        else:
            temp = self.next
            self.next = new_node
            new_node.prev = self
            new_node.next = temp
            temp.prev = new_node

# Creating nodes
node3 = DoubleLinkedListNode(3, None, None)
node2 = DoubleLinkedListNode(2, node3, None)
node3.prev = node2
node1 = DoubleLinkedListNode(1, node2, None)
node2.prev = node1

# Printing the initial nodes
print("Initial nodes:")
print(node1)
print(node2)
print(node3)

# Adding a new node using push()
node0 = DoubleLinkedListNode(0, None, None)
node1.push(node0)

# Printing the updated nodes
print("\nNodes after pushing a new node:")
print(node0)
print(node1)
print(node2)
print(node3)

