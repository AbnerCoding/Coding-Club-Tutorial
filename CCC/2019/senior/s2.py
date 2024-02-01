def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lines = int(input())
num_list = []
ans_list = []

for line in range(lines):
    num_list.append(int(input()))

for num in num_list:
    temp = []
    for i in range(2, num * 2):
        if isPrime(i) and isPrime(num * 2 - i):
            temp.append((i, num * 2 - i))
            break

    ans_list.append(temp[0])

for i in ans_list:
    print(f"{i[0]} {i[1]}")
