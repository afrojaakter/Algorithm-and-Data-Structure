#Reverse an array of integers.
def reverseArray(a):
    newArr = []
    for i in range(len(a)-1, -1, -1):
        newArr.append(a[i])
    return newArr
        
