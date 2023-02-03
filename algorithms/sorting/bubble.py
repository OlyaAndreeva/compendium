list = [2, 5, 1, 4, 3]

def bubble(to_sort):
    for i in range(len(to_sort)-1):
        for j in range(len(to_sort)-i-1):
            if to_sort[j] > to_sort[j+1]:
                swap(to_sort, j, j+1)

def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp


print("before sort: ", list)
bubble(list)
print("after sort: ", list)