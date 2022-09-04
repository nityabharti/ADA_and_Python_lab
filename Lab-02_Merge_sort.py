"""
Implement merge sort algorithm with all necessary functions.
"""

def merge(low,high):
    res = [] # for storing result
    i ,j=0,0
    # merging algorithm
    while i<len(low) and j < len(high):  
        if(low[i]<high[j]):
           res.append(low[i])
           i +=1
        else:
           res.append(high[j]) 
           j +=1
    res +=low[i:]
    res +=high[j:]
    return res


def mergesort(lst):
    if(len(lst)<=1): # return is lst has only one value, cause it is already sorted
       return lst
    mid = int(len(lst)/2)
    low = mergesort(lst[:mid]) #calling function recursively
    high = mergesort(lst[mid:])#calling function recursively
    return merge(low,high)

arr = [6,8,10,20,-40,80,-10,-4,50]
print(mergesort(arr))