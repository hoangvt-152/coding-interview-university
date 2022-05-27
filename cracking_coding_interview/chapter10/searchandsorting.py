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

def is_anagram(s1,s2):
    pass

def get_keys(s,key_to_pos):
    result = -1
    for key in key_to_pos:
        if is_anagram(s,key):
            result = key_to_pos[key]
            break
    return result    

def group_anagrams(arrays):
    marked_array = [-1 for i in range(0,len(arrays))]
    key_to_pos = dict()
    for i in range(0,len(arrays)):
        pos = get_keys(arrays[i],key_to_pos)
        if pos < 0:
            key_to_pos[arrays[i]] = i
            marked_array[i] = 1
        else:
            marked_array[pos] +=1
            marked_array[i] = pos 


#  abc = 5 6 7 1 2 3 4| 5 6 7
               
#        0 1 2 3 4 5 6  7 8 9


def get_index_of_min_item(array):
    if len(array)  <=0: return -1
    if len(array) == 1 : return 0
    min_item_index = 0    
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            min_item_index = i
            break
    return min_item_index        
def search_rotated_array(array,value):
    min_item_index = get_index_of_min_item(array)
    index = binary_search_array(min_item_index,len(array)+ min_item_index -1,array,value)
    return index

def binary_search_array(start,end,array,value):
    middle = (int((start + end)/2) + 1) % len(array)
    if start > end: 
        return -1

    if value == array[middle]:
        return middle
    if value < array[middle]:
        return binary_search_array(start,middle-1,array,value)
    else:  
        return binary_search_array(middle+1,end,array,value)       



rotatedSortedArray = [5, 6, 7, 1, 2, 3, 4]
index = search_rotated_array(rotatedSortedArray,3)
print(index)