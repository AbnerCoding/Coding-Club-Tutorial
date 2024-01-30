def get_x(num_list):
    return num_list.index("x")

num_list = []
for iter in range(3):
    num_list.append(input().split(" "))

t = 0

for nums in num_list:
    for string in range(0,len(nums)):
        if nums[string] == "x":
            if string == 1:
                t = ((int(nums[2]) - int(nums[0]))/2)
                nums[1] = str((int(nums[0])+t))[0:-2]
            if string == 0:
                t = int(nums[2]) - int(nums[1])
                nums[0] = str((int(nums[1])-t))[0:-2]
            if string == 2:
                t = int(nums[1]) - int(nums[0])
                nums[2] = str((int(nums[1])+t))[0:-2]

print(num_list)