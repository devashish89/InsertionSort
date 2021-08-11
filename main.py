# Insertion sort - similar to way we sort cards
# put marker after 1st element ==> 9|8,6,4,5,7
# 8,9|6,4,5,7
# 6,8,9|4,5,7
# 4,6,8,9|5,7
# 4,5,6,8,9|7
# 4,5,6,7,8,9|

def swap_list_elements(lst_ele, i, j):
    lst_ele[i], lst_ele[j] = lst_ele[j], lst_ele[i]


def insertionSort(lst_ele):
    start = 1
    while start < len(lst_ele):
        for i in range(start, 0, -1):
            if lst_ele[i] < lst_ele[i - 1]:
                swap_list_elements(lst_ele, i, i - 1)
                # print(lst_ele, start)

        start += 1


if __name__ == '__main__':
    lst = [9, 8, 6, 4, 5, 7]
    insertionSort(lst)
    print(lst)
