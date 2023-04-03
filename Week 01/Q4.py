def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i 
    return(sum)
arr=[]
n=len(arr)
ans=_sum(arr)
print('sum of the array is',ans)