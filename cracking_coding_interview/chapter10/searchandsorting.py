#10.1
def mergeSortedArrays(sortedA,sortedB):
    sortedMergedArray= list()
    lenA = len(sortedA)
    lenB = len(sortedB)
    i = 0
    j = 0
    current_sorted_element_number = 0
    while (current_sorted_element_number < (lenA + lenB)):
        print("ccc:"+str(current_sorted_element_number))
        print( "lenA: {} lenB:{} ".format(i,j))
        if (i == lenA and j<lenB ):            
            for jb in range(j,lenB):
                sortedMergedArray.append(sortedB[jb])
                current_sorted_element_number += 1
            j = lenB
            continue    
        if (j == lenB  and i <lenA):
            for ia in range(i,lenA):
                sortedMergedArray.append(sortedA[ia])
                current_sorted_element_number += 1
            i =lenA 
            continue    
        if sortedA[i] <= sortedB[j]:
            sortedMergedArray.append(sortedA[i])
            i += 1
            current_sorted_element_number += 1

        else:
            sortedMergedArray.append(sortedB[j])
            j +=1
            current_sorted_element_number += 1
    return sortedMergedArray        



sortedA = [1,3,5,5]
sortedB =  [2,4,6]

mergedArray = mergeSortedArrays(sortedA,sortedB)

for i in mergedArray:
    print(i)