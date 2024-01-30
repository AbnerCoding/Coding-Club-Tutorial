def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        swap = False
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                
        if not swap:
            break
        
    return arr
    
def get_diff(arr):
    length = len(arr)
    li = []
    ans = []
    for i in range(0, length-1):
        li.append(arr[i+1]-arr[i])
    length_li = len(li)
    for i in range(0, length_li-1):
        ans.append(((li[i]+li[i+1])/2))

    return ans

times = int(input())
l = []

for i in range(0, times):
    l.append(int(input()))

sorted_list = bubble_sort(l)

l = get_diff(sorted_list)
ans = min(bubble_sort(l))
print(ans)