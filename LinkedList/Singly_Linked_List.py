
class Node(object):
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;
    def setData(self, data):
        self.data = data;
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next

class LinkedList(object):
    def __init__(self):
        self.head=None
    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.getData(),end=" ")
            temp=temp.getNext()
        print()
    def insertAtBegining(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            newNode.setNext(temp)
            self.head=newNode
    def insertAtEnd(self, data):
        newNode=Node(data)
        temp=self.head
        if temp==None:
            print("Please insert values at Begining First")
        else:
            while(temp.next != None):         
                temp=temp.next
            temp.next=newNode
    def insertAtBetween(self,data1,data):
        newNode=Node(data)
        temp=self.head
        if temp==None:
            print("Please insert values at Begining First")
        else:
            while temp.data!=data1:
                temp=temp.next
            NextNode=temp.next
            temp.next=newNode
            newNode.next=NextNode
        
    def findLength(self):
        temp=self.head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count
    def deleteAtBegining(self):
        temp=self.head
        if temp==None:
            print("Please insert values at Begining First")
        else:
            temp=temp.next
            self.head=temp
    def deleteAtLast(self):
        temp=self.head
        if temp==None or temp.next==None:
            temp=None
        else: 
            while temp.next!=None:
                prev=temp
                temp=temp.next
            prev.next=None
    def deleteNode(self,data):
        temp=self.head
        if temp==None:
            print("Please insert values at Begining First")
        else:
            while temp.data!=data:
                prev=temp
                temp=temp.next
            prev.next=temp.next
        
        
            
            
            
            
        
        
        
        
        
        
            
ll=LinkedList()
ll.insertAtBegining(23)
ll.insertAtEnd(24)
ll.insertAtEnd(25)
ll.insertAtEnd(26)
ll.insertAtEnd(27)
ll.insertAtEnd(28)
ll.insertAtEnd(29)
ll.deleteNode(27)
ll.printLinkedList()
print(ll.findLength())
        
        
        
        
