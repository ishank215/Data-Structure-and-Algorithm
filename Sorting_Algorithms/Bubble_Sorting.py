class BubbleSort:
    
    def __init__(self):
        self.arr=[]
        pass
    
    # arr=[12, 34, 56, 21, 32, 76]
    
    def bubbleSort(self,arr):
        self.arr=arr
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr        
            

arr=[12, 34, 56, 21, 32, 76]
BS=BubbleSort()   
print(BS.bubbleSort(arr))
        
