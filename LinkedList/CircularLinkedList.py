class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        temp=self.head
        new_node.next=self.head
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        else:
            new_node.next=new_node
        self.head=new_node
    def printlist(self):
        temp=self.head
        if(self.head is not None):
            while(temp):
                print(temp.data)
                temp=temp.next
                if(temp==self.head):
                    break
        else:
            return
    def remove(self,key):
        if self.head.data==key:
            temp=self.head
            if(temp.next==self.head):
                temp=None
                self.head=None
                return
            else:
                while(temp.next!=self.head):
                    temp=temp.next
                temp.next=self.head.next
                self.head=self.head.next
        else:
            temp=self.head
            prev=None
            while(temp.next!=self.head):
                prev=temp
                temp=temp.next
                if(temp.data==key):
                    prev.next=temp.next
                    temp=temp.next
    def countNode(self):
        temp=self.head
        count=0
        while(temp):
            count=count+1
            temp=temp.next
            if(temp==self.head):
                break
        print(count)
    def tocircular(self,head):
        start=head
        while(head.next is not None):
            head=head.next
        head.next=start
        return

if __name__=='__main__':
    clist=CLinkedList()
    clist.push('A')
    clist.push('B')
    clist.push('C')
    #clist.printlist()
    #clist.countNode()
    clist.remove('B')
    clist.remove('A')
    clist.remove('C')
    clist.printlist()
    clist.countNode()
                
