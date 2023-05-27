array = [5,4,1,8,7,2,6,3,9]

def mergeSort_(a,b):
    print("arreglo a" + str(a) +"arreglo b" +str(b))
    finalLength = len(a)+ len(b)
    #print(finalLength)
    merged = []
    counterA = 0
    counterB = 0

    for i in range(finalLength):
        
        if counterA < len(a) and (counterB >= len(b) or a[counterA] <= b[counterB]):
            print("se agrego a")
            merged.append(a[counterA])
            counterA += 1
        else:
            print("se agrego b")
            merged.append(b[counterB])
            counterB += 1
        print(merged)
    return merged

   
        


def mergeSort(array):
    sizeArray = len(array)
    if sizeArray <= 1:  
        return array
    
    halfArray = (len(array)//2)
    a = array[0:halfArray]
    b = array[halfArray:] 

    a = mergeSort(a)
    b = mergeSort(b)

    return mergeSort_(a,b)

print(mergeSort(array))
    