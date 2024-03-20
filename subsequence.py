from typing import List

def is_subset(main_set:List,sub_set:List)->bool:
    """checks whether a certain sub set of a main list is part of that list and the 
     sublist must be of the same order as the main list.
     "this is the WHILE loop implementation.

    Args:
        main_set (List): main list that contains the all the lists
        sub_set (List): may or may not be sublist of the main list

    Returns:
        bool: wether the sublist is a true sublist or not
    """
    pointer_main=0
    pointer_sub=0
    print(f"total length is {len(main_set)}")
    while pointer_sub<=len(sub_set)-1 and pointer_main<=len(main_set)-1:
        #print(f"subset_po:{pointer_sub} and main_po {pointer_main}")..used for debugging
        if sub_set[pointer_sub] == main_set[pointer_main]:
            pointer_main+=1
            pointer_sub+=1
        else:
            pointer_main+=1

    if pointer_sub==len(sub_set):
        return True
    else:
        return False
    

def is_subset_2(main_set,sub_set):
    pointer=0
    for i in main_set:
        if pointer==len(sub_set):
            break

        if i == sub_set[pointer]:
            pointer+=1
    return pointer==len(sub_set)

p=[12,77,45,32,12,34,45,56,64,43,23,12,76]
s_p=[23,12]
is_it=is_subset_2(p,s_p)
print(f"is it nor not: {is_it}")
