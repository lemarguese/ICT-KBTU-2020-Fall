n = int(input())
i = 0
count = 0
while n != 1:
    i += 1
    n -= 1
    if n % i == 0:
        print(n, i)
        count += 1
print(count)

