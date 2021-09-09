# Insertion sort - similar to way we sort cards
# put marker after 1st element ==> 9|8,6,4,5,7
# 8,9|6,4,5,7 # before pipe would be sorted and each element after pipe is inserted into sorted array before pipe
# 6,8,9|4,5,7
# 4,6,8,9|5,7
# 4,5,6,8,9|7
# 4,5,6,7,8,9|

def insertionSort(lst):
    n = len(lst)
    for i in range(1,n):
        x = lst[i]
        # ulta loop left of marker(|) to run from i-1 to 0 with steps -1 to
        # check if new lst[i] can be inserted in sorted array before marker (|)
        for j in range(i-1, -1, -1):
            if x < lst[j]:
                lst[j], lst[j+1] = x, lst[j]



if __name__ == '__main__':
    lst = [9, 8, 6, 4, 5, 7]
    insertionSort(lst)
    print(lst)
