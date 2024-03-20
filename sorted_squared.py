def sorted_squared(sorted_list):
    #abs_lists=[abs(i) for
    squared_list=[i**2 for i in sorted_list]
    new_ordered=sorted(squared_list)
    return new_ordered

#smarter way of handling this situation is
def sorting_linear_time(sorted_array):
    new_array=[]
    start=0
    end=len(sorted_array)-1
    while True:
        if abs(sorted_array[start]) > abs(sorted_array[end]):
            new_array[]

#test mechanism
lis=[-3,-2,1,4]
print(f"\noriginal value is:{lis}")
print(f" altered value is :{sorted_squared(lis)}")