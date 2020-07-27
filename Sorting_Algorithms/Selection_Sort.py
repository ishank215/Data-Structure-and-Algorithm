
# iterative method
def selectionSort(arr):
    for i in range(len(arr)-1): 
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
    
    
arr=[23, 67, 45, 12, 70, 61, 87]
print(selectionSort(arr))

    
