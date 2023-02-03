list = [1, 2, 4, 3, 5] # 1 -> 4 length=5

def insertion(to_sort):
    for i in range(1, len(to_sort)): # range(start_inclusive, end_exclusive, step)
        j = i
        while j > 0 and to_sort[j] < to_sort[j - 1]:
            swap(to_sort, j, j - 1)
            j = j - 1

def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp


print("before sort: ", list)
insertion(list)
print("after sort: ", list)