nums = list(map(int, input().split()))

even_sum = 0
odd_sum = 0

for n in nums:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print(even_sum, odd_sum)