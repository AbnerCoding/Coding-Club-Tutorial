def isPrime(num):
    yPrime = False
    if num == 1:
        return yPrime
    if num > 1:
        for iter in range(2, num):
            if num % iter == 0:
                yPrime = True
                break

        if yPrime:
            return 0
        else:
            return 1

lines = int(input())
num_list = []
ans_list = []


for line in range(lines):
    num_list.append(int(input()))

for num in num_list:
    temp = []
    for i in range(0, num*2):
        for j in range(0, num*2):
            if isPrime(i) and isPrime(j):
                if (i + j)/2 == num:
                    temp.append((i, j))
                    break
                else:
                    continue
        if len(temp) != 0:

            ans_list.append(temp[0])
            break
        else:
            continue

for i in ans_list:
    print(str(i[0]) + ' ' + str(i[1]))