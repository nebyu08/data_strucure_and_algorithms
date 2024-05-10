def cloest_value_target_BST(target,tree,closest=float('inf')):
    """finds the closes value to a target value in a binary search tree

    Args:
        target (int): the number we looking we find in the tree or closes number to it
        tree (tree): the tree we are going to search number for
        current_best (int, optional): best value so far in the tree during search
    """

    current_node=tree
    while current_node is not None:
        if abs(target-closest) > abs(target-current_node.value):
            closest=current_node.value

        if target > current_node.value:
            current_node=current_node.right
        elif target < current_node.value:
            current_node=current_node.left
        else:   #this is exectuted if we find the eact number in the tree hence there is no need to traverse 
            break

    return closest