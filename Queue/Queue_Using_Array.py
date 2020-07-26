
class Queue:
    def __init__(self):
        self.arr=[]
    def insert(self,data):
        self.arr.append(data)
    def delete(self):
        if len(self.arr)==0:
            print("Queue is Empty!")
        else:
            for i in range(1,len(self.arr)):
                self.arr[i-1]=self.arr[i]
            self.arr=self.arr[0:len(self.arr)-1]
    def display(self):
        for i in self.arr:
            print(i,end=" ")
        print()
    
q=Queue()
q.insert(23)
q.insert(24)
q.insert(25)
q.delete()
q.display()
