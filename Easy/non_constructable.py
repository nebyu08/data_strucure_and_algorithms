def non_constructable(given_list):
    """extract the minimum amount of number that we can make from the list that is given to us

    Args:
        given_list (given_list): given distribution of numbers
    """
    given_list.sort()
    change=0
    for i in given_list:
        if i>change+1:
            return change+1
        change+=i

    return change+1



temp_list=[1,2,5]
print(f"things we can't find in the list:{non_constructable(temp_list)}")