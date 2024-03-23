def sorted_squared(sorted_list):
    #abs_lists=[abs(i) for
    squared_list=[i**2 for i in sorted_list]
    new_ordered=sorted(squared_list)
    return new_ordered

#smarter way of handling this situation is
def sorting_linear_time(sorted_array):
    """the solutions should be arranged on incresing order from left to right
    meaning that the smallest number is on the far left side while the biggest 
    is on the far right.

    Args:
        sorted_array (list): this is order list(array)
    """
    new_array=[0 for _ in sorted_array]
    start=0
    end=len(sorted_array)-1
    for i in reversed(range(len(sorted_array))):
        smallest=sorted_array[start]
        biggest=sorted_array[end]
        if abs(smallest)>abs(biggest):
            new_array[i]=smallest**2
            start+=1
        else:
            new_array[i]=biggest**2
            end-=1
    return new_array  

#test mechanism
lis=[-3,-2,10,20,40]
print(f"\noriginal value is:{lis}")
print(f" altered value is :{sorting_linear_time(lis)}")