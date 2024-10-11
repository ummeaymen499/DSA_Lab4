def Partition(arr,):
   i,j=0,0
   pivot=arr[-1]
   while i<len(arr) and j<len(arr):
      if(arr[j]<=pivot):
         arr[j],arr[i]=arr[i],arr[j]
         i+=1
         j+=1
      elif(arr[j]>pivot):
         j+=1
   return i-1
arr=[8,7,1,3,5,6,4]
i=Partition(arr)
print(i)

print(arr)         
            
    pivot=A[r-1]
    i=p-1
    j=p
    for j in range(r):
       if(A[j]<=pivot):
           A[j],A[i]=A[i],A[j]
           i+=1 
    A[i+1]=A[r-1]
    return i+1        