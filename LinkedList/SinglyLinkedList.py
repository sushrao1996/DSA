class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_value):
        new_node = Node(new_value)
        new_node.next= self.head
        self.head=new_node
    def insertAt(self,prev_node,new_value):
        if prev_node is None:
            print("Previous node is empty")
        new_node = Node(new_value)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head=new_node
            return
        tmp=self.head
        while(tmp.next):
            tmp=tmp.next
        tmp.next=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        if temp==None:
            return "Linked List is empty"
    def deleteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        prev=None
        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
    def deleteTotalList(self):
        curr=self.head
        while curr:
            self.head=curr.next
            del curr.data
            curr=self.head
    def getNodeCount(self,node):
        if(not node):
            return 0
        else:
            return 1 +self.getNodeCount(node.next)
    def getCount(self):
        return self.getNodeCount(self.head)
    def LinkedReverse(self):
        prev=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
          
if __name__=='__main__':
    llist=LinkedList()
    llist.append(4)
    llist.push(3)
    llist.push(5)
    llist.append(7)
    llist.append(6)
    llist.deleteNode(7)
    llist.printlist()
    print(llist.getCount())
    llist.LinkedReverse()
    llist.printlist()
    llist.deleteTotalList()
    llist.printlist()
    llist
        
