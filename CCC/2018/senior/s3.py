def calc_empty_space(arr):
    rov_pos = None
    empty = []
    length = len(arr)
    for i in range(length):
        for j in range(len(arr[i])):
            if arr[i][j] == "S":
                rov_pos = [i, j]
            elif arr[i][j] == ".":
                empty.append([i, j])
    return rov_pos, empty



N, M = input().split(" ")[0:2]

N = int(N)
M = int(M)

maze = []

for i in range(N):
    maze.append(input()[0:M])


ans = []

rov_pos, empty = calc_empty_space(maze)

p = rov_pos
n = 0
s = 0
step = 0
while s < len(empty):
    step = 0
    while n < len(empty):
        e = empty
        bad = False
        for i in e:
            print(i, rov_pos)
            if i[0] == rov_pos[0]:
                rov_pos[1] = i[1]
                e.pop(e.index(rov_pos))
                step += 1
            elif i[1] == rov_pos[1]:
                rov_pos[0] = i[0]
                e.pop(e.index(rov_pos))
                step += 1
        if e[0][0] != rov_pos[0] and e[0][1] != rov_pos[1]:
            ans.append(-1)                
        n += 1
        ans.append(step)

        
    s += 1
print(ans)