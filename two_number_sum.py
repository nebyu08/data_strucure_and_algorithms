# lets solve for the 2 sum numbers ...in many ways
import numpy as np

#solving it with much space and time complexity
def twosumnum(array,target):
    '''this will run on:
    O(n2):big O of n squred in time complexity,
    O(n):bing O of n in space complexity
    '''
    for i in range(len(array)-1):
        first_num=array[i]
        for j in range(i+1,len(array)):
            second_num=array[j]
            if first_num+second_num==target:
                return [first_num,second_num]
    return []


array=[3,5,-4,8,11,1,-1,6]

print("using high space and time complexity")
print(twosumnum(array,10))

#lets solve it using hash table

def hash_table_soln(array,target):
    hash_table={}
    for i in range(len(array)):
        current=array[i]
        y=target-current
        if y in hash_table:
            return [y,current]
        else:
            hash_table[current]=True

        # for i in hash_table:
        #     if y==i:
        #         return [x,y]
        #     else:
        #         hash_table[current]=True
    return []


print("using hash but the code is a bit clumsy:")
print(hash_table_soln(array,10))


#lets reqrite the above code in efficent way
def using_hash_table(array,target):
    ''' this will run on O(n) in space and time complexity'''
    nums={}
    for num in array:
        y=target-num  #the target minus the current value we are in our list of codes
        if y in nums:
            return [y,num]
        else:
            nums[num]=True
    return []


print("also hash but the code is clean:")
print(using_hash_table(array,10))



def sorting_matching(array:np.ndarray,target):
    array.sort(kind="mergesort")
    for i in range(len(array)):
        front=array[i]  #this points to the front part of the array
        end= array[len(array)-1]  #this points to the last part of the array
        if (front+end)==target:
            return [front,end]
        elif (front+end)<target:
            front+=1
        elif (front+end)>target:
            end-=1
    return []

print("using sorting and searching algotith:")
np_array=np.array([3,5,-4,8,11,1,-1,6])
print(sorting_matching(np_array,10))

#lets optimize the above code 
def efficent_two_sum(array:np.ndarray,
                     target):
    '''this complexity of the code is:
     space complexity is "O(nlogn)"
     time complexity "O(1)"
    '''
    array.sort(kind="mergesort")
    front=0
    back=len(array)-1

    while front<back:
        current_sum=array[front]+array[back]
        if (current_sum==target):
            return [array[front],array[back]]
        elif (current_sum<target):
            front+=1
        elif (current_sum>target):
            target-=1
    return []

print("the most efficent algorith for this problem is:")