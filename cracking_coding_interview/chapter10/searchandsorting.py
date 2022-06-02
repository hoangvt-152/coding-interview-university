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
    index = binary_search_array(min_item_index,len(array)+ min_item_index -1,array,value,min_item_index)
    return index

def binary_search_array(start,end,array,value,min_index):
    middle = int((start + end)/2) % len(array)
    if start > end: 
        return -1

    if value == array[middle]:
        return middle
    new_start = middle    
    if middle < min_index:
        new_start = middle + len(array)    
    if value < array[middle]:
        return binary_search_array(start,new_start-1,array,value,min_index)
    else:  
        return binary_search_array(new_start+1,end,array,value,min_index)       


#10.5
def closest_not_empty_string_index(current_index,array):
    if array[current_index] !="":
        return current_index,current_index
    left   = -1
    right = -1
    for i in range(1,current_index+1):
        if array[current_index-i] !="":
            left = current_index -i
            break
    for i in range(1,len(array) -current_index+1-1):
        if array[current_index+i] !="":
            right = current_index +i
            break
    return left,right        
  

def find_string_interset(array,value,start,end):
    if start >end:
        return -1
    middle = int((start + end)/2)
    print("middle:{}".format(middle))
    if array[middle] == value:
        return middle
    
  
    lef_index,right_index = closest_not_empty_string_index(middle,array)
    
    print("lef_index:{}--right_index:{}".format(lef_index,right_index))

    if  value <= array[lef_index]:
        return find_string_interset(array,value,start,lef_index) 
    
    if array[lef_index] <value and value < array[right_index]:
        return -1
    
    if array[right_index] <= value:
        return find_string_interset(array,value,right_index,end)


#rotatedSortedArray = [5, 6, 7, 1, 2, 3, 4]
#index = search_rotated_array(rotatedSortedArray,4)
#print(index)

#10.8 sortedMatrixSearch


def  binary_search_matrix(matrix,value,col1,col2,row1,row2):
    pass
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y    
            
def sortedMatrixSearch(matrix,point1,point2,value):
    result = list()
    if matrix[point1.x][point1.y] > value or value > matrix[point2.x][point2.y]:
        return result
    if point1 == point2:
        if matrix[point1.x][point1.y] == value:
            result.append(point1)
        return result

    x = int((point1.x + point2.x)/2)
    y = int((point1.y + point2.y)/2)
    
    if matrix[x][y] == value:
        r1 = sortedMatrixSearch(matrix,Point(x,point1.y),Point(point2.x,y),value)
        r2 = sortedMatrixSearch(matrix,Point(point1.x,y),Point(x,point2.y),value)
        return result + r1 + r2

    if matrix[x][y] > value:
        r1 = sortedMatrixSearch(matrix,Point(x,point1.y),Point(point2.x,y),value)
        r2 = sortedMatrixSearch(matrix,Point(point1.x,y),Point(x,point2.y),value)
        r3 = sortedMatrixSearch(matrix,point1,Point(x,y),value)
        return result + r1 + r2 +r3
    if matrix[x][y] < value:
        r1 = sortedMatrixSearch(matrix,Point(x,point1.y),Point(point2.x,y),value)
        r2 = sortedMatrixSearch(matrix,Point(point1.x,y),Point(x,point2.y),value)
        r3 = sortedMatrixSearch(matrix,Point(x,y),point2,value)
        return result + r1 + r2 +r3    

A = [[1 ],
      [],
      [],
      [],
      ]        


         

array = ["at","","","","ball","","","","car"]

index = find_string_interset(array,"car",0,len(array)-1)
print(index)