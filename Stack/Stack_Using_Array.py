
class Stack:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.arr=[0 for i in range(self.size)]
        
    def push(self,data):
        if self.top==self.size-1:
            raise ValueError("Stack Overflow")
        else:
            self.top+=1
            self.arr[self.top]=data
    def peek(self):
        return self.arr[self.top]
    def pop(self):
        if self.top==-1:
            raise ValueError("Stack Overflow")
        else:
            self.top=self.top-1
    def display(self):
        for i in range(self.top+1):
            print(self.arr[i],end=" ")
        print()
            
    
s=Stack(5)
s.push(23)
s.push(24)
s.push(25)
s.push(26)
s.push(27)

print(s.peek())
s.display()
