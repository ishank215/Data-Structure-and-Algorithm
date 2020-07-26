
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.previous=None
    def insert(self,data):
        newNode=Node(data)
        if self.front==None:
            self.front=newNode
            self.rear=self.front
        else:
            self.previous=self.front
            self.front.next=newNode
            self.front=self.front.next
            self.front.prev=self.previous
    def delete(self):
        if self.rear==None:
            print("Queue is Empty!")
        else:
            self.rear=self.rear.next
            self.rear.prev=None
    def display(self):
        temp=self.rear
        while temp.data!=self.front.data:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
        print()
        
        
q=Queue()
q.insert(23)
q.insert(24)
q.insert(25)
q.delete()
print(q.front.data)
q.display()
        
            
        