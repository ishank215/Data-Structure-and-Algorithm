
def quickSort(arr,beg,end):
    loc=0
    if beg<end:
        loc=partition(arr,beg,end)
        quickSort(arr,beg,loc-1)
        quickSort(arr,loc+1,end)

def partition(arr,left,right):
    loc=left
    flag=0
    while flag==0:
        while arr[loc]<=arr[right] and loc!=right:
            right=right-1
        if loc==right:
            flag=1
        elif arr[loc]>arr[right]:
            arr[loc],arr[right]=arr[right],arr[loc]
            loc=right
        else:
            pass
        if flag==0:
            while arr[loc]>=arr[left] and loc!=left:
                left=left+1
            if loc==left:
                flag=1
            elif arr[loc]<arr[left]:
                arr[loc],arr[left]=arr[left],arr[loc]
                loc=left
            else:
                pass
    return loc

arr=[23,455,12,63,7324,73]
quickSort(arr,0,5)
print(arr)

