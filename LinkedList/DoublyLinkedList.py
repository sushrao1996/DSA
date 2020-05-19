class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_value):
        new_node=Node(new_value)
        new_node.next=self.head
        if (self.head is not None):
            self.head.prev=new_node
        self.head=new_node
    def insertAfter(self,prev_node,new_value):
        new_node=Node(new_value)
        if prev_node is None:
            print("Previous node cannot be empty")
            return
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
    def append(self,new_value):
        new_node=Node(new_value)
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        else:
            temp=self.head
            while (temp.next is not None):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def deleteNode(self,key):
        cur=self.head
        while cur:
            if cur.data==key and cur==self.head:
                if not cur.next:
                    cur.data=None
                    self.head=None
                    return
                else:
                    nxt=cur.next
                    cur.next=None
                    cur.prev=None
                    cur=None
                    self.head=nxt
                    return
            elif cur.data==key:
                if cur.next:
                    nxt=cur.next
                    prev=cur.prev
                    prev.next=nxt
                    nxt.prev=prev
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    prev=cur.prev
                    prev.next=None
                    cur.prev=None
                    cur=None
                    return
            cur=cur.next
    def countNodes(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
            
dlist=DoublyLinkedList()
dlist.push(3)
dlist.push(4)
dlist.push(5)
dlist.append(6)
dlist.insertAfter(dlist.head.next,8)
dlist.append(11)
print(dlist.countNodes())
dlist.deleteNode(5)
dlist.printlist()

        
                
            
                
