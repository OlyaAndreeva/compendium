list = [1, 7, 4, 9, 2, 3] 

def merge(to_sort):
    if len(to_sort) > 1:
        left_list = to_sort[:len(to_sort)//2] # [start_inc:end_exc:step] -> 0, 1
        right_list = to_sort[len(to_sort)//2:len(to_sort)]
        # print(to_sort, "->", left_list, " + ", right_list)

        merge(left_list)
        merge(right_list)

        i1 = 0
        i2 = 0
        i = 0
        while i1 < len(left_list) and i2 < len(right_list):
            if left_list[i1] < right_list[i2]:
                to_sort[i] = left_list[i1]
                i1 = i1 + 1
                i = i + 1
            else:
                to_sort[i] = right_list[i2]
                i2 = i2 + 1
                i = i + 1
        while i2 < len(right_list):
            to_sort[i] = right_list[i2]
            i2 = i2 + 1 
            i = i + 1
        while i1 < len(left_list):
            to_sort[i] = left_list[i1]
            i1 = i1 + 1
            i = i + 1
            
        

print("before sort: ", list)
merge(list)
print("after sort: ", list)