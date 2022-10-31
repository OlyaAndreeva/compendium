# Given list=[0,1,2,3,4,5] reverse it using while loop

list=[10,20,30,40,50,100]
print("list",list)
left = 0
right = len(list)-1
while left<right:
    temp = list[right]  # temp = 100
    list[right] = list[left] # [10,20,30,40,50,10]
    list[left] = temp # [100,20,30,40,50,10]
    left = left+1
    right = right-1
print("list_result",list)