
def mergeSort(arr,beg,end):
    
    if beg<end:
        mid=(beg+end-1)//2
        mergeSort(arr,beg,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,beg,mid,end)
        
def merge(arr,beg,mid,end):
    leftArray=[]
    rightArray=[]
    n1=mid-beg+1
    n2=end-mid
    for i in range(n1):
        leftArray.append(arr[beg+i])
    for j in range(n2):
        rightArray.append(arr[mid+1+j])
    i=0
    j=0
    k=beg
    while i<n1 and j<n2:
        if leftArray[i]<=rightArray[j]:
            arr[k]=leftArray[i]
            i+=1
        else:
            arr[k]=rightArray[j]
            j+=1
        k+=1    
        

    while i<n1:
        arr[k]=leftArray[i]
        k+=1
        i+=1
    while j<n2:
        arr[k]=rightArray[j]
        k+=1
        j+=1
        
        
        
        
arr=[23, 56, 71, 98, 12, 98, 23, 87, 87]
mergeSort(arr,0,len(arr)-1)
print(arr)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        



