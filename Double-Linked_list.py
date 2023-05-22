class DoubleLinkedListNode(object):
   def __init__(self, value, nxt, prev):
       self.value = value
       self.next = nxt
       self.prev = prev
       
       
   def __repr__(self):
       nval = self.next and self.next.value or None 
       pval = self.prev and self.prev.value or None
      
       return f"[{self.value}, {repr(nval)}, {repr(pval)}]"
 
node3 = DoubleLinkedListNode(3, None, None)
node2 = DoubleLinkedListNode(2, node3, None)
node3.prev = node2
node1 = DoubleLinkedListNode(1, node2, None)
node2.prev = node1

print(node1)
print(node2)
print(node3)     
  
