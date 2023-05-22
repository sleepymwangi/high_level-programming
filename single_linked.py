class singlelinkednode(object):
    
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
    
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

node1 = singlelinkednode(3, None)
node2 = singlelinkednode(2, node1)
node3 = singlelinkednode(1, node2)

print(node1)
print(node2)
print(node3)

