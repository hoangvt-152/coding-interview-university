

def triple_step(n):
    if n <0: return 0
    if n == 0: return 1
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)




def power_set(total,current_subset,number_of_elements,current_index):
    if current_index == number_of_elements:
        total.append(current_subset)
        return
    for i in range(0,2):
        current_subset[current_index]=i 
        power_set(total,current_subset,number_of_elements,current_index+1)

def ps(n):
    current_subset = [0 for i in range(0,n)]
    all_subset = list()
    power_set(all_subset,current_subset,n,0)
    return all_subset


def pathensis(n):
   all_syntax = list()
   for i in range(1,n+1):
        