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

N = int(input())

data = []

for i in range(N):
    data.append((input().split(" "))[0:N])

new_data = []

for i in data:
    new_data.append(bubble_sort(i))

revert_data = []
l = []

for i in range(0, N):
    for j in range(0, N):
        l.append(new_data[j][i])
    revert_data.append(l)
    l = []

ans = []
for i in range(N):
    ans.append(bubble_sort(revert_data[i]))

for i in ans:
    print(' '.join(map(str, i)))